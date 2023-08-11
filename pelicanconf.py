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
SOCIAL = (('GitHub', 'https://youareeverysingleday.github.io'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# 设置使用的样式模板。
THEME = 'theme/gum'
# PLUGIN_PATHS = ['plugin']
# PLUGINS = ['assets']
# 设置需要取的静态文件（图片）的路径。
STATIC_PATHS = ['images']

# 删除输出目录，然后 all 在生成新文件之前。这有助于防止旧的、不必要的文件保留在输出中。
# 然而， 这是一个破坏性的设置，应该非常小心地处理。
DELETE_OUTPUT_DIRECTORY = True

# 是否在模板的菜单上显示类别。模板可能不支持此设置。
DISPLAY_CATEGORIES_ON_MENU = True

# 是否在模板的菜单上显示页面。模板可能不支持此设置。
DISPLAY_PAGES_ON_MENU = True

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

GITHUB_URL = 'https://youareeverysingleday.github.io'

# OUTPUT_PATH = '../youareeverysingleday.github.io/'
# RELATIVE_URLS = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True