from pathlib import Path

from ruamel.yaml import YAML

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
