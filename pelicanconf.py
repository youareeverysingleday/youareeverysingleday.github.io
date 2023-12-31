# 主要设置一些在本地验证时的配置。并且在发布时也会使用。
# publishconf.py中的配置会覆盖pelicanconf.py中的配置。

AUTHOR = 'youareeverysingleday'
SITENAME = 'Coder'
SITEURL = 'https://youareeverysingleday.github.io'
# 设置页面子标题。
SITESUBTITLE = 'You are every single day.'

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# 删除输出目录，然后 all 在生成新文件之前。这有助于防止旧的、不必要的文件保留在输出中。
# 然而， 这是一个破坏性的设置，应该非常小心地处理。
DELETE_OUTPUT_DIRECTORY = True


# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None

# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('GitHub', 'https://youareeverysingleday.github.io'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# 如果未在post元数据中指定类别，请将此设置设置为 True ，
# 并将文章组织到子文件夹中，则该子文件夹将成为您文章的类别。如果设置为 False ， DEFAULT_CATEGORY 将用作备用。
USE_FOLDER_AS_CATEGORY = False

# 要依赖的默认类别。
DEFAULT_CATEGORY = 'Commonknowledge'

# 是否在模板的菜单上显示页面。模板可能不支持此设置。
DISPLAY_PAGES_ON_MENU = True

# 是否在模板的菜单上显示类别。模板可能不支持此设置。
DISPLAY_CATEGORIES_ON_MENU = True

FEED_ALL_RSS =  'feeds/all.rss.xml'

# 设置使用的样式模板。
THEME = 'theme/gum'
PLUGIN_PATHS = ['plugins']

# 暂时不适用category_meta插件。因为这个插件的使用要求：“our articles should not have a Category: 
# tag in their metadata; instead, they should be stored in 
# (subdirectories of) per-category directories.”
# 也就是说要求md文件中不能含有Category元数据。这个要求很奇怪。
PLUGINS = ['tag_cloud', 'more_categories', 'autopages', 'sitemap']
# 设置需要取的静态文件（图片）的路径。
STATIC_PATHS = ['images']

# 设置站点地图。
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "monthly",
        "pages": "monthly",
    }
}

# 使用google anlytics分析网站数据。
GOOGLE_ANALYTICS_ID = 'G-MZN76F9MXF'

# 包含日志记录级别的元组列表（最多 warning )以及要忽略的信息。
import logging
LOG_FILTER = [(logging.WARN, 'TAG_SAVE_AS is set to False')]

# 降价处理器的额外配置设置。请参阅Python Markdown文档 Options section 以获取支持选项的完整列表。
# 这个 extensions 选项将自动从 extension_configs 选择权。
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# 生成文件的输出位置。这应该与web服务器的虚拟主机根目录相对应。
OUTPUT_PATH = 'docs/'

# github站点的网址。
GITHUB_URL = 'https://youareeverysingleday.github.io'

# 当尝试使用不同的设置（尤其是元数据设置）时，缓存可能会干扰，
# 并且更改可能不可见。在这种情况下，请确保通过禁用缓存 LOAD_CONTENT_CACHE = False 或者使用 --ignore-cache 命令行开关。
LOAD_CONTENT_CACHE = False


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True