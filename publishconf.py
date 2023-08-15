# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

# 主要设置一些需要在互联网环境中使用的配置。比如评论、订阅等。
# publishconf.py中的配置会覆盖pelicanconf.py中的配置。

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
# 网站的基本URL。默认情况下没有定义，因此最好指定您的SITEURL；如果不这样做，
# 则不会使用格式正确的URL生成提要。如果您的站点可通过HTTPS访问，则此设置应以 
# https:// -否则使用 http:// . 然后附加你的域，结尾不带斜杠。例子： SITEURL = 'https://example.com'
SITEURL = 'https://youareeverysingleday.github.io'
RELATIVE_URLS = False

# 订阅相关的设置。
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'


# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""