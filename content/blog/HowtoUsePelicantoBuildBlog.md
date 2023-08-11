Title: 如何使用Pelican创建一个博客
Date: 2023-08-11
Category: Commonknowledge
Tags: blog,pelican
Slug: pelican-brochure
Author: youareeverysingleday

# HowtoUsePelicantoBuildBlog

## experience

1. 常用命令，
   1. 命令参考<https://www.osgeo.cn/pelican/>。
   2. 流程参考<https://zhuanlan.zhihu.com/p/614277442>。
   
      |编号|命令|作用|说明|
      |---|---|---|---|
      |1|pelican-quickstart|填写pelican基本信息。后期可以通过pelicanconf.py修改。|进入页面目录|
      |2|pelican content|生成网站。|需要content目录下已经有按照规则撰写的markdown文档。|
      |3|pelican --listen|打开新的终端会话，导航到项目根目录，然后运行以下命令以启动Pelican的web服务器。|CTRL+C退出的时候反应会比较慢。|
      |4||||
      |5||||
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

## problems

1. 无法显示latex公式。
2. gum样式没有显示category和page。

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
3. 操作参考<https://jlhxxxx.github.io/pelican-github.html>。
4. 中文pelican手册<https://www.osgeo.cn/pelican/plugins.html>。
5. 需要添加pelican-plusin
   1. 添加了assets始终报错：CRITICAL UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb2 in position 8: invalid     __init__.py:566                    start byte
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

