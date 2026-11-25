# oobeyagroup.com

Source for https://oobeyagroup.com. Django templates rendered to static HTML and published with GitHub Pages.

## Making a change

1. Create a branch: `git checkout -b my-change`
2. Edit templates in `oobeyagroup/templates/oobeyagroup/`
3. Preview: `.venv/bin/python manage.py runserver`, then open http://localhost:8000
4. Push and open a pull request: `git push -u origin my-change`. A check builds the site; wait for the green tick.
5. Merge into `main`. The site is rebuilt and published in about a minute.

To undo a published change, use **Revert** on the merged pull request.

## First-time setup

    python3 -m venv .venv
    .venv/bin/pip install -r requirements-build.txt

## How publishing works

`build_site.py` renders each page and collects static files into `_site/`. The workflow in `.github/workflows/pages.yml` runs it on every push to `main` and deploys to GitHub Pages.
