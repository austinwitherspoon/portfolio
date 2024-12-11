AUTHOR = "Austin Witherspoon"
SITENAME = "Austin Witherspoon | Blog"
SITEURL = "http://austinwitherspoon.com"
SITETITLE = "Austin Witherspoon"
SITESUBTITLE = "Filmmaker | Software Developer"

# SITELOGO = SITEURL + "/images/profile.png"
FAVICON = "static/favicon.ico"

BROWSER_COLOR = "#333"
PATH = "content"

TIMEZONE = "America/Los_Angeles"

DEFAULT_LANG = "English"

CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

FEED_ALL_RSS = "feeds/all.rss.xml"
CATEGORY_FEED_RSS = "feeds/{slug}.rss.xml"

DISPLAY_PAGES_ON_MENU = False
# Blogroll
LINKS = (
    ("home", "/"),
    ("blog", "/blog_index.html"),
)
INDEX_SAVE_AS = "blog_index.html"

# Social widget
SOCIAL = (
    ("youtube", "https://www.youtube.com/channel/UCzHlz1lU53PK531OWRVwatQ"),
    ("github", "https://github.com/austinwitherspoon"),
    ("twitter", "https://twitter.com/ajwitherspoon"),
    ("instagram", "https://www.instagram.com/austinjwitherspoon"),
    ("mastodon", "https://mastodon.social/@austinwitherspoon"),
    ("rss", "/feeds/all.atom.xml"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "themes/Flex"
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["summary", "search"]

STATIC_PATHS = ["static", "extra"]
EXTRA_PATH_METADATA = {
    "extra/index.html": {"path": "index.html"},
    "extra/gazoonkas.html": {"path": "gazoonkas.html"},
}
ARTICLE_EXCLUDES = ['static', "extra"]
CUSTOM_CSS = "static/custom.css"

MAIN_MENU = True
MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

# ADD_THIS_ID = "ra-77hh6723hhjd"
# DISQUS_SITENAME = "yoursite"
# GOOGLE_ANALYTICS = "UA-1234-5678"
# GOOGLE_TAG_MANAGER = "GTM-ABCDEF"
THEME_COLOR = "dark"
# THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
# THEME_COLOR_ENABLE_USER_OVERRIDE = True

PYGMENTS_STYLE = "emacs"
PYGMENTS_STYLE_DARK = "monokai"

COPYRIGHT_YEAR = "2023 Austin Witherspoon"
USE_LESS = True
