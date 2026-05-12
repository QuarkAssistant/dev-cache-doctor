import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
README = (ROOT / "README.md").read_text(encoding="utf-8")

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.buttons = []
        self.links = []
        self.scripts = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "button":
            self.buttons.append(attrs)
        if tag == "a":
            self.links.append(attrs.get("href", ""))
        if tag == "script":
            self.scripts.append(attrs.get("src"))

parser = Parser()
parser.feed(HTML)

def test_required_product_elements_present():
    required = [
        "Dev Cache Doctor",
        "Share this tool",
        "https://ko-fi.com/quarkassistant",
        "Built by Quark Assistant — autonomous AI agent. Code authored by AI under owner supervision.",
        "No uploads",
        "no analytics",
        "Next.js",
        "Vite",
        "Docker",
        "WATCHPACK_POLLING",
        "CHOKIDAR_USEPOLLING",
        "serviceWorker",
        "lockfile",
        "Copy issue note",
        "CI cache key sanity pack",
        "ciCacheSnippet",
        "incidentNote",
        "devCommands",
        "viteForceCommands",
    ]
    for text in required:
        assert text in HTML

def test_no_remote_javascript_or_analytics():
    assert "https://www.googletagmanager.com" not in HTML
    assert "google-analytics" not in HTML.lower()
    assert all(src in (None, "") for src in parser.scripts)

def test_share_and_kofi_affordances():
    assert any("ko-fi.com/quarkassistant" in href for href in parser.links)
    assert "navigator.share" in HTML
    assert "clipboard.writeText" in HTML

def test_readme_disclosure_and_privacy():
    assert "No analytics" in README
    assert "No external JavaScript" in README
    assert "Built by Quark Assistant" in README
    assert "https://quarkassistant.github.io/dev-cache-doctor/" in README
    assert "GitHub issue note" in README
    assert "CI cache-key drift" in README

def test_html_has_title_and_description():
    assert re.search(r"<title>Dev Cache Doctor", HTML)
    assert re.search(r'<meta name="description" content="[^"]+stale Next.js/Vite', HTML)

if __name__ == "__main__":
    tests = [name for name in globals() if name.startswith("test_")]
    for name in tests:
        globals()[name]()
        print(f"ok {name}")
    print(f"{len(tests)} tests passed")
