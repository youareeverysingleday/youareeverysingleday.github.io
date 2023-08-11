# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

# 主要设置一些需要在互联网环境中使用的配置。比如评论、订阅等。
# publishconf.py中的配置会覆盖pelicanconf.py中的配置。

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *


SITEURL = 'https://youareeverysingleday.github.io'
RELATIVE_URLS = False

# 订阅相关的设置。
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'


# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""