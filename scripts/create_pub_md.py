import os
import sys
import string
import calendar
from datetime import datetime
from pathlib import Path
import shutil

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



def create_pub_bundle(bib_path, pub_dir):
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

    date = datetime.utcnow()
    timestamp = date.isoformat("T") + "Z"  # RFC 3339 timestamp.

    title = clean_bibtex_str(entry["title"])
    pub_date = extract_year(entry)
    year = pub_date.split('-')[0]
    authors = entry["author"]
    authors = clean_bibtex_authors([i.strip() for i in authors.replace("\n", " ").split(" and ")])

    output_path = Path(pub_dir) / year / slugify(authors, year, title, words_from_title=3)
    output_path.mkdir(parents=True, exist_ok=True)

    index_md_path = Path(output_path)/'index.md'

    write_index_md(index_md_path, entry, authors, title, pub_date, timestamp)
    cite_key = slugify(authors, year, title, words_from_title=1)
    shutil.copy(bib_path, output_path / f'{cite_key}.bib')
    print(f"Remember to add to {output_path}: \n  1. a figure\n  2. a PDF of the paper")


def write_index_md(index_md_path, entry, authors, title, pub_date, timestamp):
    page = EditableFM(Path(index_md_path))

    page.fm["title"] = title
    page.fm["date"] = pub_date
    page.fm["publishDate"] = timestamp

    for bib_detail in ['volume', 'issue', 'number', 'pages']:
        if bib_detail in entry:
            page.fm[bib_detail] = entry[bib_detail]

    page.fm["authors"] = authors
    page.fm["abstract"] = clean_bibtex_str(entry["abstract"])

    # Publication name.
    if "booktitle" in entry:
        publication = clean_bibtex_str(entry["booktitle"])
    elif "journal" in entry:
        publication = clean_bibtex_str(entry["journal"])
    elif "publisher" in entry:
        publication = clean_bibtex_str(entry["publisher"])
    else:
        raise ValueError("No venue specified, if preprint add the service, e.g. arXiv, SSRN")
    page.fm["publication"] = publication

    if "url" in entry:
        page.fm["url_pdf"] = clean_bibtex_str(entry["url"])

    if "doi" in entry:
        page.fm["doi"] = clean_bibtex_str(entry["doi"])


    page.fm["featured"] = False
    page.fm["sg-areas"] = None

    # Save Markdown file.
    page.dump()


def extract_year(entry):
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

    return "-".join([year, month, day])




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
            raise ValueError("Please update the entry with a valid month.")


def slugify(authors, year, title, words_from_title=3):
    lastname = authors[0].split(' ')[-1]  # first authors surname
    title = clean_bibtex_str(title)
    title = ''.join([c for c in title if c in string.ascii_letters+' '])
    title = title.split(' ')[:words_from_title]
    short_title = '-'.join(title)
    key = f'{lastname}{year}{short_title}'
    return key.lower()


if __name__ == "__main__":
    create_pub_bundle(sys.argv[1], sys.argv[2])
