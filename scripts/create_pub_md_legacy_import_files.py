import os
import sys
import string
import calendar
from datetime import datetime
from pathlib import Path

from ruamel.yaml import YAML

import bibtexparser
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.customization import convert_to_unicode


yaml = YAML()


class EditableFM:
    def __init__(self, path: Path, dry_run: bool = False):
        self.fm = dict()
        self.content = []
        self.path = path
        self.dry_run = dry_run

    def dump(self):
        assert self.path, "You need to `.load()` first."
        if self.dry_run:
            return

        with open(self.path, "w", encoding="utf-8") as f:
            f.write("{}\n".format('---'))
            yaml.dump(self.fm, f)
            f.write("{}\n".format('---'))
            f.writelines(self.content)



def parse_bibtex_file(bib_path):
    if not Path(bib_path).is_file():
        raise ValueError("Not a File.")

    with open(bib_path, 'r') as bib_file:
        parser = BibTexParser(common_strings=True)
        parser.customization = convert_to_unicode
        parser.ignore_nonstandard_types = False
        bib_database = bibtexparser.load(bib_file, parser=parser)

        assert len(bib_database.entries) == 1, \
            f"bib file should contain 1 entry, but {len(bib_database.entries)} found."

        entry = bib_database.entries[0]
        output_path = os.path.dirname(bib_path)
        create_pub_index(entry, output_path, featured=False)

def create_pub_index(
    entry, output_path, featured=False
):
    """Parse a bibtex entry and generate corresponding publication bundle"""

    date = datetime.utcnow()
    timestamp = date.isoformat("T") + "Z"  # RFC 3339 timestamp.

    Path(output_path).mkdir(parents=True, exist_ok=True)

    index_md_path = Path(output_path)/'index.md'

    page = EditableFM(Path(index_md_path))

    # breakpoint()
    page.fm["title"] = clean_bibtex_str(entry["title"])

    year, month, day = "", "01", "01"
    if "date" in entry:
        dateparts = entry["date"].split("-")
        if len(dateparts) == 3:
            year, month, day = dateparts[0], dateparts[1], dateparts[2]
        elif len(dateparts) == 2:
            year, month = dateparts[0], dateparts[1]
        elif len(dateparts) == 1:
            year = dateparts[0]
    if "month" in entry and month == "01":
        month = month2number(entry["month"])
    if "year" in entry and year == "":
        year = entry["year"]
    if len(year) == 0:
        raise ValueError("Year is not available.")

    page.fm["date"] = "-".join([year, month, day])

    for bib_detail in ['volume', 'issue', 'number', 'pages']:
        if bib_detail in entry:
            page.fm[bib_detail] = entry[bib_detail]

    page.fm["publishDate"] = timestamp

    authors = entry["author"]

    authors = clean_bibtex_authors([i.strip() for i in authors.replace("\n", " ").split(" and ")])
    page.fm["authors"] = authors
    if 'abstract' in entry:
        page.fm["abstract"] = clean_bibtex_str(entry["abstract"])
    else:
        page.fm["abstract"] = ''


    # Publication name.
    if "booktitle" in entry:
        publication = clean_bibtex_str(entry["booktitle"])
    elif "journal" in entry:
        publication = clean_bibtex_str(entry["journal"])
    elif "publisher" in entry:
        publication = clean_bibtex_str(entry["publisher"])
    else:
        publication = ""
    page.fm["publication"] = publication

    if "url" in entry:
        page.fm["url_pdf"] = clean_bibtex_str(entry["url"])

    if "doi" in entry:
        page.fm["doi"] = clean_bibtex_str(entry["doi"])


    page.fm["featured"] = featured
    page.fm["sg-areas"] = None

    # Save Markdown file.
    page.dump()
    return page


def clean_bibtex_authors(author_str):
    """Convert author names to `firstname(s) lastname` format."""
    authors = []
    for s in author_str:
        s = s.strip()
        if len(s) < 1:
            continue

        if "," in s:
            split_names = s.split(",", 1)
            last_name = split_names[0].strip()
            first_names = [i.strip() for i in split_names[1].split()]
        else:
            split_names = s.split()
            last_name = split_names.pop()
            first_names = [i.replace(".", ". ").strip() for i in split_names]

        if last_name in ["jnr", "jr", "junior"]:
            last_name = first_names.pop()

        for item in first_names:
            if item in ["ben", "van", "der", "de", "la", "le"]:
                last_name = first_names.pop() + " " + last_name

        authors.append(" ".join(first_names) + " " + last_name)

    return authors


def clean_bibtex_str(s):
    """Clean BibTeX string and escape TOML special characters"""
    s = s.replace("\\", "")
    s = s.replace('"', '\\"')
    s = s.replace("{", "").replace("}", "")
    s = s.replace("\t", " ").replace("\n", " ").replace("\r", "")
    return s


def month2number(month):
    """Convert BibTeX or BibLateX month to numeric"""

    if len(month) <= 2:  # Assume a 1 or 2 digit numeric month has been given.
        return month.zfill(2)
    else:  # Assume a textual month has been given.
        month_abbr = month.strip()[:3].title()
        try:
            return str(list(calendar.month_abbr).index(month_abbr)).zfill(2)
        except ValueError:
            raise log.error("Please update the entry with a valid month.")


def slugify(author_surname, year, title, words_from_title=3):
    lastname = author_surname.lower()
    title = clean_bibtex_str(title)
    title = title.split(' ')[:words_from_title]
    title = ''.join([c for c in title if c in string.ascii_letters])
    short_title = '-'.join(title).lower()
    key = f'{lastname}{year}{short_title}'
    return key


if __name__ == "__main__":

    parse_bibtex_file(sys.argv[1])
