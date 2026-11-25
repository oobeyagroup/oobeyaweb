"""Render the Django site to plain static files for GitHub Pages.

Usage:  python build_site.py [output_dir]   (default: _site)

Each page is rendered through Django's test client, written as an .html file
(GitHub Pages serves /oobeyagroup/agileandscrum from agileandscrum.html), and
static assets are collected next to it under /static/.
"""
import os
import shutil
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
OUT = Path(sys.argv[1] if len(sys.argv) > 1 else BASE_DIR / "_site").resolve()
DOMAIN = "oobeyagroup.com"

os.environ["STATIC_BUILD"] = "1"
os.environ["STATIC_BUILD_ROOT"] = str(OUT / "static")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oobeyaweb.settings")
sys.path.insert(0, str(BASE_DIR))

import django  # noqa: E402

django.setup()

from django.core.management import call_command  # noqa: E402
from django.template.loader import render_to_string  # noqa: E402
from django.test import Client  # noqa: E402

PAGES = [
    "/",
    "/oobeyagroup/agileandscrum",
    "/oobeyagroup/technologyleadership",
    "/oobeyagroup/productmanagement",
    "/oobeyagroup/softwaredevelopment",
]


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    call_command("collectstatic", interactive=False, verbosity=0)

    client = Client()
    for path in PAGES:
        resp = client.get(path)
        if resp.status_code != 200:
            raise SystemExit(f"{path} returned {resp.status_code}")
        target = OUT / "index.html" if path == "/" else OUT / (path.strip("/") + ".html")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(resp.content)
        print(f"wrote {target.relative_to(OUT)}")

    (OUT / "404.html").write_text(render_to_string("oobeyagroup/404.html", {"request": None}))
    (OUT / "CNAME").write_text(DOMAIN + "\n")
    (OUT / ".nojekyll").write_text("")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: https://{DOMAIN}/sitemap.xml\n")
    urls = "\n".join(f"  <url><loc>https://{DOMAIN}{p}</loc></url>" for p in PAGES)
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n'
    )
    print(f"site built in {OUT}")


if __name__ == "__main__":
    main()
