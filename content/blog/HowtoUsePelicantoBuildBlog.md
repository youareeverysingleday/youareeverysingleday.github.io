Title: 如何使用Pelican创建一个博客
Date: 2023-08-11
Category: Commonknowledge
Tags: blog,pelican
Slug: pelican-brochure
Author: youareeverysingleday

## experience

1. 常用命令，
   1. 命令参考<https://www.osgeo.cn/pelican/>。
   2. 流程参考<https://zhuanlan.zhihu.com/p/614277442>。
   
      |顺序|命令|作用|说明|
      |---|---|---|---|
      |1|pelican-quickstart|填写pelican基本信息。后期可以通过pelicanconf.py修改。|进入页面目录|
      |2|pelican content|生成网站。|需要content目录下已经有按照规则撰写的markdown文档。|
      |3|pelican --listen|打开新的终端会话，导航到项目根目录，然后运行以下命令以启动Pelican的web服务器。|CTRL+C退出的时候反应会比较慢。|
      |4|/|使用一个主题||
      |5|/|增加blog的功能，也就是增加blog的插件。||
      |6|/|将更新之后的blog更新到github上。|到此基本步骤完成。后期的使用主要在于如何增加各种插件和使用何种模板上。|
      |7|/|||


   3. 创建的markdown文档开头的格式及说明：
   
      |名称|描述|
      |---|---|
      |title|文章或页的标题|
      |date|出版日期（例如。， YYYY-MM-DD HH:SS ）|
      |modified|修改日期（例如。， YYYY-MM-DD HH:SS ）|
      |tags|内容标记，用逗号分隔|
      |keywords|内容关键字，用逗号分隔（仅限HTML内容）|
      |category|内容类别（仅一个-不是多个）|
      |slug|URL和翻译中使用的标识符|
      |author|内容作者，当只有一个时|
      |authors|当有多个|
      |summary|索引页内容简述|
      |lang|内容语言ID (en ， fr 等）|
      |translation|如果内容是另一个的翻译 (true 或 false ）|
      |status|内容状态： draft ， hidden 或 published|
      |template|用于生成内容的模板的名称（不带扩展名）|
      |save_as|将内容保存到此相对文件路径|
      |url|用于此文章/页面的URL|

   4. pelicanconf.py中的配置

      |编号|参数|说明|
      |---|---|--- |
      ||STATIC_PATHS = ['images']|通过上文，我们已经成功添加第一篇博客，但是很快会发现，如果你往content目录里面添加一个images文件夹存放博文的图片，你会发现pelican content并不会复制images文件夹到output目录下。这种不需要编译但又要用到的文件，我们称它为“静态文件”。pelican默认不会复制静态文件到output目录，需要我们在pelicanconf.py配置文件上面配置一下,添加该行。|
      ||SITEURL|也要设置成Pages的地址|
      ||||
      ||||
      ||||
2. pelican的模板
   1. 首先通过<https://pelicanthemes.com/>查看模板的样式，这个里面有粗略编译之后的样式，具体的需要看代码里面的展示。
   2. 通过<https://github.com/getpelican/pelican-themes>下载代码。
   3. 通过<https://www.osgeo.cn/pelican/pelican-themes.html>查看安装theme的命令。
   4. 将下载下来的模板代码拷贝到python安装库目录下的文件夹中。相对Python的目录为：Python\Lib\site-packages\pelican\themes。直接复制到该目录下之后，通过pelican-themes -v -l就可以看到安装好的模板了。
3. 可以使用根目录下的某个文件夹作为github pages的发布路径。目前github pages只能使用docs/作为发布路径。。"Optionally, use the folder dropdown menu to select a folder for your publishing source."
4. publishconf.py和pelicanconf.py的区别？也就是说一般都在pelicanconf.py中进行配置。
   1. 在publishconf.py中定义的内容将覆盖pelicanconf.py中的相同定义。作为Pelican设置文件首先将分为两部分，考虑两种主要的操作模式：本地开发和生产部署（分别为pelicanconf.py和publishconf.py）。不建议将GOOGLE_ANALYTICS从pelicanconf.py移动publishconf.py到。在本地开发时，Google Analytics 和 Disqus 等设置在设计上pelicanconf.py将被故意排除。pelicanconf.py在本地测试中包含这些设置可能会产生不利影响：不准确的站点统计数据、虚假评论线程以及其他意外的副作用。但请注意，publishconf.py仅在两种情况下使用：
   2. 当您使用make publish（或其他 make 命令之一）生成站点时。
   3. 当您明确指定它作为要使用的配置文件时（即pelican -s publishconf.py content_dir）。因此，如果您使用命令生成站点pelican，并且没有明确指定您的配置文件，则只会pelicanconf.py使用；因此你需要将GOOGLE_ANALYTICS变量设置在那里。
   4. 注意publishconf.py和pelicanconf.py的区别。在pelicanconf.py中不要设置SITEURL，因为设置之后就会导致在本地调试的时候重新生成文章的链接是SITEURL设置的远程地址。
5. 暂时不使用category_meta插件。因为这个插件的使用要求：“our articles should not have a Category: tag in their metadata; instead, they should be stored in (subdirectories of) per-category directories.” 也就是说要求md文件中不能含有Category元数据。这个要求很奇怪。
6. favicon.ico放在output（也就是生成最终静态页面的目录下）的根目录下。这样就不会报：“WARNING  Unable to find `/favicon.ico` or variations: ”的错误了。
7. 注意在使用了图片的文章里面需要修改图片的引用路径。
8. 使用pandoc将markdown转换为word。
   1. pandoc下载：<https://github.com/jgm/pandoc/releases/tag/3.1.7>
   2. 官方网站：<https://pandoc.org/installing.html>
   3. 转化命令需要在pandoc.exe所在目录下使用。转换命令为：pandoc.exe test.md -f markdown -t docx -s -o test.docx  
   4. 命令说明：文件名 test.md 是要转换的源文件；-f 设置输入文件的格式；-t 设置输出文件的格式；-s 表示创建一个“独立”文件，将会生成文件页眉和页脚。默认的转换格式为 markdown 到 word，所以上面的命令也可以省略这两个选项。
   5. pandoc将markdow转化为word时太复杂的公式和符号无法转换。


## problems

1. ~~无法显示latex公式。~~
   1. 解决这个问题的方法不是让pelican解决的，而是通过chrome插件来解决的。使用chrome的TeX All the Things插件就可以很好的显示所有页面中的latex公式。
   2. 但是TeX All the Things插件对矩阵的表现非常差，mathjax的显示效果最好。
2. gum样式没有显示category、page和~~tags~~。
   1. 使用tags需要使用tag_cloud插件。
3. 生成的时候如何将favicon.ico也生成在静态文件的根目录下。
4. ~~本地调试页面的时候，发现具体的文章页面的路径是SITEURL+文章Slug组成的绝对路径。~~
   1. 通过使用RELATIVE_URLS = True来解决。

## references

### 放弃使用jekyll

1. 简单页面部署<https://zhuanlan.zhihu.com/p/28321740>。
2. 部署能解析markdown的blog<https://zhuanlan.zhihu.com/p/102346113>。
3. jekyll多种模板<http://jekyllthemes.org/>。
4. HTML5静态页面模板<https://html5up.net/>。
5. rtd模板<https://github.com/readthedocs/sphinx_rtd_theme>。

### pelican

1. 入门参考。它是使用python编译的，并且支持markdown。<https://zhuanlan.zhihu.com/p/55603083>。
2. 重要参考2<https://zhuanlan.zhihu.com/p/614277442>。
   1. 这个参考更详细：<https://maxwell-nc.github.io/blog/pelicanBuildBlog.html>。
   2. 这个参考有深度，包含了如何让搜索引擎搜索和Google Analytics的内容<https://www.cnblogs.com/cciejh/p/blog_building.html>。感觉Google Analytics主要用于开店的，展示不使用。
3. 操作参考<https://jlhxxxx.github.io/pelican-github.html>。
4. 中文pelican手册<https://www.osgeo.cn/pelican/plugins.html>。
5. 需要添加pelican-plusin
   1. 添加了assets始终报错：
      ```log
      CRITICAL UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb2 in position 8: invalid     __init__.py:566                    start byte
      ```
6. 模板参考：
   1. 展示：<https://pelicanthemes.com/>。
   2. 代码：<https://github.com/getpelican/pelican-themes>。
   3. 有几个备选的模板，其中选中<https://pelicanthemes.com/pelican-twitchy/>。
      1. <https://pelicanthemes.com/gum/>可以。首要备选。
      2. <https://pelicanthemes.com/dev-random3/>可以，比较直接。
      3. <https://pelicanthemes.com/relapse/>可以。
      4. <https://pelicanthemes.com/mg/>这个搜索框没有作用。还比较简洁。
      5. <https://pelicanthemes.com/foundation-default-colours/>可以。但是没有分类在两边。
      6. <https://pelicanthemes.com/bootstrap/category/misc.html>可以。但是没有分类在两边。
      7. <https://pelicanthemes.com/notmyidea-cms-fr/>可以，主要是背景颜色不太喜欢。
7. 插件plugins：<https://github.com/getpelican/pelican-plugins>。很多模板都需要安装了插件之后才能使用完整功能。
   1. markdown显示latex插件：<https://github.com/kitelife/pelican_plugin-latex/>。
8. 让bing和google能够搜索到blog。
   1. bing
      1. 打开bing webmaster<https://www.bing.com/webmasters/home>。
      2. 登录bing。
      3. 使用在页面中添加标记的方式验证。修改生成的index.html，在<body>之前的<head>中添加<meta name="msvalidate.01" content="AAAA" />代码作为验证标识。让bing webmaster验证即可。
   2. google
      1. <meta name="google-site-verification" content="EEEE" />
9. 生成网站地图。使用的是sitemap插件。在pelicanconf.py中设置sitemap的含义如下：The SITEMAP setting must be a Python dictionary and can contain these keys:
   - format, which sets the output format of the plugin (xml or txt)
   - priorities, which is a dictionary with three keys:
      - articles, the priority for the URLs of the articles and their translations
      - pages, the priority for the URLs of the static pages
      - indexes, the priority for the URLs of the index pages, such as tags, author pages, categories indexes, archives, etc.
      All the values of this dictionary must be decimal numbers between 0 and 1.
   - changefreqs, which is a dictionary with three items:
      - articles, the update frequency of the articles
      - pages, the update frequency of the pages
      - indexes, the update frequency of the index pages
      Valid frequency values are always, hourly, daily, weekly, monthly, yearly and never.
   - exclude, which is a list of regular expressions that will be used to exclude matched URLs from the sitemap if any of them match. 
10. google站长工具使用参考<https://zhuanlan.zhihu.com/p/432637356>。参考价值不高。
11. 使用Google Analytics<https://www.kovlala.fun/2021/08/Howto-use-google-analytics-with-Python-Pelican.html>。好的参考。
    1. 登录到 Google Analytics，创建账号，生成新的Property。
    2. 使用 MEASUREMENT ID写入pelicanconf.py中。设置GOOGLE_ANALYTICS_ID = 'XXXXXX'变量。
    3. 修改Theme中base.html文件。添加Google Analytics中提供的js代码。
    4. 设置完成，更新线上Pelican的Article，约0.5小时后可登录GA后台查看结果。

