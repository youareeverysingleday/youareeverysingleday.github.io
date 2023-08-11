# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = ''
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

# 删除输出目录，然后 all 在生成新文件之前。这有助于防止旧的、不必要的文件保留在输出中。
# 然而， 这是一个破坏性的设置，应该非常小心地处理。
DELETE_OUTPUT_DIRECTORY = True

# 是否在模板的菜单上显示类别。模板可能不支持此设置。
DISPLAY_CATEGORIES_ON_MENU = True

# 是否在模板的菜单上显示页面。模板可能不支持此设置。
DISPLAY_PAGES_ON_MENU = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""