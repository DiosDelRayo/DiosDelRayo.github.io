# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

AUTHOR = 'DiosDelRayo'
SITENAME = ''
# SITEURL = "https://diosdelrayo.github.io"

PATH = "content"

TIMEZONE = 'UTC'
DEFAULT_LANG = 'en'
GITHUB='https://github.com/DiosDelRayo'
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
ARTICLE_PATHS = ['articles']
USE_FOLDER_AS_CATEGORY = True
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = 'article/{slug}.html'
CATEGORY_SAVE_AS = 'article/{slug}.html'
GITHUB = 'https://github.com/DiosDelRayo'
DEFAULT_DATE = 'fs'

DELETE_OUTPUT_DIRECTORY = True


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
    'taskstack'
]
# Blogroll
LINKS = (
    ("GitHub", "https://github.com/DiosDelRayo"),
)

# Social widget
SOCIAL = (
)

DEFAULT_PAGINATION = False
