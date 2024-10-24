# with open('.GITHUB_TOKEN', 'r') as f:
#     GITHUB_TOKEN=f.read()
#     f.close()


AUTHOR = 'DiosDelRayo'
SITENAME = ''
SITEURL = ''

PATH = 'content'

TIMEZONE = 'UTC'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
RELATIVE_URLS = True
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
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
# TAG_CLOUD_BADGE = True

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
    ('Github DiosDelRayo', 'https://github.com/DiosDelRayo'),
    ('Pelican TaskStack Plugin', 'https://getpelican.com'),
    ('TaskStack', 'https://github.com/DiosDelRayo/taskstack'),
    ('Pelican TaskStack Plugin', 'https://github.com/DiosDelRayo/pelican-taskstack'),
    ('Site Source', 'https://github.com/DiosDelRayo/DiosDelRayo.github.io'),
)

# Social widget
SOCIAL = (
)

DEFAULT_PAGINATION = False
