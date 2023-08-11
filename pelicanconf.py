AUTHOR = 'youareeverysingleday'
SITENAME = 'youareeverysingleday.Blog'
SITEURL = 'https://youareeverysingleday.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = 'theme/gum'
# PLUGIN_PATHS = ['plugin']
# PLUGINS = ['assets']
STATIC_PATHS = ['images']

# 
DELETE_OUTPUT_DIRECTORY = True

# 是否在模板的菜单上显示类别。模板可能不支持此设置。
DISPLAY_CATEGORIES_ON_MENU = True

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

# OUTPUT_PATH = '../youareeverysingleday.github.io/'
# RELATIVE_URLS = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True