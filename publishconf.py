# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
# SITEURL = "https://diosdelrayo.github.io"
PATH = "content"
ARTICLE_PATHS = ['projects']
USE_FOLDER_AS_CATEGORY = True
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
TIMEZONE='UTC'
AUTHOR='DiosDelRayo'
GITHUB='https://github.com/DiosDelRayo'
DEFAULT_DATE='fs'
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
ARTICLE_PATHS = ['projects']
USE_FOLDER_AS_CATEGORY = True
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = 'project/{slug}.html'
CATEGORY_SAVE_AS = 'project/{slug}.html'
GITHUB = 'https://github.com/DiosDelRayo'
DEFAULT_DATE = 'fs'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.toc': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.tables': {},
        'markdown.extensions.fenced_code': {},
        'markdown.extensions.footnotes': {},
        'markdown.extensions.attr_list': {},
        'markdown.extensions.def_list': {},
        'markdown.extensions.abbr': {},
        'markdown.extensions.nl2br': {},
        'markdown.extensions.smarty': {},
        'markdown.extensions.abbr': {},
        'markdown.extensions.sane_lists': {},
        'markdown.extensions.md_in_html': {},
        'markdown.extensions.toc': {},
        'markdown.extensions.wikilinks': {},
        'pymdownx.mark': {},
        'pymdownx.emoji': {},
        'pymdownx.progressbar': {},
        'pymdownx.tilde': {},
        'pymdownx.tasklist': {},
    }
}

PLUGINS = [
]

ANALYTICS = """
<style>
ul.checkbox li {
    list-style-type: none;
}
</style>
"""
# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

