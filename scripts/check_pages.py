"""Check generated page coverage and compile every inline JavaScript block with Node."""
from html.parser import HTMLParser
import json
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET

from f1stats.generate import DOCS_DIR, PAGES


class InlineScripts(HTMLParser):
    def __init__(self):
        super().__init__()
        self.scripts = []
        self.current = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "script" and "src" not in attrs:
            if attrs.get("type", "text/javascript") in ("text/javascript", "application/javascript", "module"):
                self.current = []

    def handle_data(self, data):
        if self.current is not None:
            self.current.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self.current is not None:
            self.scripts.append("".join(self.current))
            self.current = None


def check_pages(directory: Path = DOCS_DIR):
    count = 0
    for name in PAGES:
        html = (directory / name).read_text()
        if "</html>" not in html:
            raise ValueError(f"Incomplete page: {name}")
        parser = InlineScripts()
        parser.feed(html)
        for index, script in enumerate(parser.scripts, start=1):
            result = subprocess.run(["node", "--check"], input=script, text=True, capture_output=True)
            if result.returncode:
                raise ValueError(f"{name}, script {index}: {result.stderr}")
            count += 1
    json.loads((directory / "data.json").read_text())
    ET.parse(directory / "sitemap.xml")
    print(f"Validated {len(PAGES)} pages, {count} JavaScript blocks, data.json, and sitemap.xml")


if __name__ == "__main__":
    check_pages()
