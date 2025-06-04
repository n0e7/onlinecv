import os
from bs4 import BeautifulSoup

import pytest

HTML_FILES = ["index.html", "Page loisir.html"]

@pytest.mark.parametrize("filename", HTML_FILES)
def test_single_html_tag(filename):
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), filename)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    soup = BeautifulSoup(content, "html.parser")
    html_tags = soup.find_all("html")
    # Ensure there is exactly one html tag
    assert len(html_tags) == 1, f"{filename} should contain exactly one <html> tag"
    # Ensure closing tag exists after opening tag by checking string search
    assert "</html>" in content.lower(), f"{filename} must contain a closing </html>"
