Title: 在离线环境下搭建硬件包含GPU的Ubuntu系统
Date: 2023-11-01
Category: MachineLearning
Tags: blog,Ubuntu,GPU
Slug: Build-Ubuntu-GPU-Offline
Author: youareeverysingleday

Building an Ubuntu system with hardware including GPU in an offline enviroment.

## 1. 总体思路

1. 使用Ubuntu启动盘安装Ubuntu。
2. 使用apt install -y按需的软件源下载。
   1. apt-mirror实在有点坑。建议弃坑。使用apt-mirror工具制作软件包的镜像，然后让ubuntu安装相关更新。
3. 使用dpkg制作离线包。

## 2. 参考

1. 重要-ubuntu下的apt内网本地源的正确搭建。使用apt-mirror工具[https://www.cnblogs.com/mlwork/p/12262819.html](https://www.cnblogs.com/mlwork/p/12262819.html)。这个工具下载了整个ubuntu需要更新的软件源。大约有150GB的大小，需要下载很长时间。
   1. 需要详细说明。特别是mirror.list的使用。
2. 没有使用。制作少量软件源的参考。
   1. [https://blog.csdn.net/qq_41037945/article/details/124440867](https://blog.csdn.net/qq_41037945/article/details/124440867)。
   2. [https://zhuanlan.zhihu.com/p/346562578](https://zhuanlan.zhihu.com/p/346562578)。
3. 安装过程中的磁盘分区
   1. 需要详细说明。特别是挂载的步骤、方式、区别。
4. 使用apt install -y和dpkg来做软件源。
   1. [https://blog.csdn.net/yiquan_yang/article/details/109670854](https://blog.csdn.net/yiquan_yang/article/details/109670854)

> 命令中的gedit就是ubuntu中的TextEditor工具。

### 2.1 sources.list文件格式说明

参考: [https://www.cnblogs.com/yahuian/p/apt-sources-list.html](https://www.cnblogs.com/yahuian/p/apt-sources-list.html)

![sources.list文件格式](../images/sourceslist_format.png "sources.list文件格式")

1. 第一部分
   deb 表示二进制可执行文件
   deb-src 表示包的源代码
2. 第二部分：URL仓库地址。一定要使用https的软件源地址。
3. 第三部分：发行版代号，ubuntu 20.04 为 focal

   ```shell
   ubuntu@VM-0-12-ubuntu:~$ lsb_release -a
   No LSB modules are available.
   Distributor ID: Ubuntu
   Description:    Ubuntu 20.04.1 LTS
   Release:        20.04
   Codename:       focal
   ```

   security 重要的安全更新
   updates 建议的更新
   proposed pre-released 更新
   backports 不支持的更新（遇到问题不一定有人修，而且可能导致系统出其他问题）
   **一般情况下，一般选择前2个即可**。
4. 第四个部分：是按照软件的自由度来区分的。一般情况下，4个全部选择即可。
   main 包是免费的/开源的，并受 ubuntu 官方的支持
   restricted 包含各种设备的专用驱动程序
   universe 包是免费的/开源的，由社区支持
   multiverse 由于法律/版权问题，这些软件包受到限制
5. 使用 sed 快速替换

   ```shell
   sed -i 's/被替换的内容/要替换成的内容/' file
   sudo sed -i 's/archive.ubuntu/mirrors.aliyun/' /etc/apt/sources.list
   ```

## 3. 使用apt install -y和dpkg来做软件源

步骤如下：

主要流程参考：[https://blog.csdn.net/magic_guo/article/details/129148074](https://blog.csdn.net/magic_guo/article/details/129148074)。

### 3.1 下载ubuntu软件和python依赖包

1. ubuntu软件源

   1. 需要下载的软件如下：

   | 编号  | 软件                | 说明                                                                                                                 | 参考                                                                                                                            |
   | ----- | ------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
   | 1必须 | openssh-server      | ubuntu上的SSH服务。                                                                                                  | <>                                                                                                                              |
   | 2必须 | sysstat             | 主要用途是观察服务负载，比如CPU和内存的占用率、网络的使用率以及磁盘写入和读取速度等。                                | [https://blog.csdn.net/sixisixsix/article/details/106430379](https://blog.csdn.net/sixisixsix/article/details/106430379)           |
   | 3必须 | net-tools           | 网络工具集，包含ifconfig命令等。                                                                                     | <>                                                                                                                              |
   | 4必须 | python3-pip         | python中的pip管理工具。                                                                                              | <>                                                                                                                              |
   | 5     | gawk                | 主要就是用来在大的数据中提取中自己需要的元素（对文本数据的每行进行处理），然后将其格式化，使得重要的数据更易于阅读。 | [https://blog.csdn.net/weixin_42119041/article/details/108735906](https://blog.csdn.net/weixin_42119041/article/details/108735906) |
   | 6     | bc                  | bc 命令是任意精度计算器语言，通常在linux下当计算器用。                                                               | [https://www.runoob.com/linux/linux-comm-bc.html](https://www.runoob.com/linux/linux-comm-bc.html)                                 |
   | 7     | unzip               | zip文件压缩、解压缩工具。                                                                                            | [https://www.cnblogs.com/cy0628/p/13903990.html](https://www.cnblogs.com/cy0628/p/13903990.html)                                   |
   | 8     | wget                | 下载文件的工具。                                                                                                     | [https://blog.csdn.net/feng98ren/article/details/102505662](https://blog.csdn.net/feng98ren/article/details/102505662)             |
   | 9     | iptables-persistent | 暂时用不到。iptables是一个linux下的防火墙工具，它能帮助我们基于规则进行网络流量控制。                                | [https://zhuanlan.zhihu.com/p/574057147](https://zhuanlan.zhihu.com/p/574057147)                                                   |
   | 10    | psmisc              | 暂时用不到。                                                                                                         | <>                                                                                                                              |
   | 11    | docker-compose      | 暂时用不到。                                                                                                         | <>                                                                                                                              |


   2. 下载之前一定使用一次apt-get upgrade和apt-get update命令。用于更新现有的软件和软件源信息。
   3. 下载之前先进入目录"/var/cache/apt/archives"下。
   4. 因为必须下载的软件并不多，所以使用逐个下载的方式下载，并且下载相关依赖。使用的下载命令如下：

      ```shell
      apt-get download $(apt-rdepends openssh-server | grep -v "^ " | sed 's/debconf-2.0/debconf/g')
      apt-get download $(apt-rdepends sysstat | grep -v "^ " | sed 's/debconf-2.0/debconf/g')
      apt-get download $(apt-rdepends net-tools | grep -v "^ " | sed 's/debconf-2.0/debconf/g')
      apt-get download $(apt-rdepends python3-pip | grep -v "^ " | sed 's/debconf-2.0/debconf/g')
      ```
   5. 直接下载时会出现如下报错：

      ```text
      Download is performed unsandboxed as root as file '/home/[Account]/adduser_3.118ubuntu2_all.deb' couldn't be accessed by user '_apt'. - pkgAcquire::Run (13: Permission denied)
      ......
      ```

      解决方法参考：[https://blog.csdn.net/bigbaojian/article/details/131117477](https://blog.csdn.net/bigbaojian/article/details/131117477)。
      使用如下命令解决，注意后面的目录是apt-get download的文件目录：

      ```shell
      sudo chown -Rv _apt:root /var/cache/apt/archives/
      sudo chmod -Rv 700 /var/cache/apt/archives/
      ```

      具体原因解释为：新版本apt-get程序开始使用_apt用户确安全。apt程序一般使用_apt用户进行软件包下载，这个提示是_apt用户没有相应文件和目录的写权限，此时文件为红色，非可执行状态。通过如下命令确保_apt用户对/var/cache/apt/archives/partial/目录及其内含的文件具备写入权限。在Ubuntu中，“sandbox user”（沙盒用户）是指一个受限制的用户账户，用于运行不受信任的程序或应用程序。沙盒用户是为了增加系统安全性而设计的，它们被限制在一个受控的环境中，无法访问敏感文件或系统资源。当你运行一个程序时，尤其是来自不受信任的来源或具有潜在安全风险的应用程序时，将其运行在沙盒用户账户下可以提供额外的保护。沙盒用户通常被配置为拥有较少的权限，限制其对系统文件和设置的访问权限。这样，即使程序被攻击或存在漏洞，攻击者也无法访问系统的关键部分。通过将程序运行在沙盒用户账户下，可以减轻潜在的安全风险，保护系统和用户的数据免受恶意软件或攻击的影响。

      注意：**此后apt download生效，但是仅一次**。每次使用4中的命令之前都需要运行一次。最终的脚本如下：

      ```shell
      sudo chown -Rv _apt:root /var/cache/apt/archives/
      sudo chmod -Rv 700 /var/cache/apt/archives/
      apt-get download $(apt-rdepends openssh-server | grep -v "^ " | sed 's/debconf-2.0/debconf/g')
      sudo chown -Rv _apt:root /var/cache/apt/archives/
      sudo chmod -Rv 700 /var/cache/apt/archives/
      apt-get download $(apt-rdepends sysstat | grep -v "^ " | sed 's/debconf-2.0/debconf/g')
      sudo chown -Rv _apt:root /var/cache/apt/archives/
      sudo chmod -Rv 700 /var/cache/apt/archives/
      apt-get download $(apt-rdepends net-tools | grep -v "^ " | sed 's/debconf-2.0/debconf/g')
      sudo chown -Rv _apt:root /var/cache/apt/archives/
      sudo chmod -Rv 700 /var/cache/apt/archives/
      apt-get download $(apt-rdepends python3-pip | grep -v "^ " | sed 's/debconf-2.0/debconf/g')
      ```
2. python依赖包
   注意现在时online环境，在使用pip之前，ubuntu必须已经安装了python3-pip软件。

   1. 安装pip。

      ```shell
      apt-get install python3-pip
      ```
   2. 要求代码所需的所有依赖包已经使用pip install命令下载完毕。
   3. 导出python依赖包清单：

      ```shell
      pip freeze >requirements.txt
      ```
   4. 将依赖包下载到指定的文件夹。

      ```shell
      pip download -r [path of Requirement.txt] -d [RequirementPath]
      ```

      path of Requirement.txt: requirement.txt的保存路径。
      RequirementPathPath: 将requirements.txt所在路径。

      示例：

      ```shell
      pip download -r requirements.txt -d /home/[account]/PythonDependencies
      ```

      在下载的过程中绝大多数情况下会报两种错误：1. 某种依赖包无法下载或者不存在。解决方法是删除requirements.txt中对应的依赖包的列，然后重新运行该命令即可。原因：在下载的过程中由于ubuntu上已经安装有python 3.8而且已经安装了部分与ubuntu直接相关的python依赖包。也就是说offline环境中和online环境中的依赖包已经存在并且版本也一致。
      2. 某种依赖包的版本不匹配。按照报错中的提示手动调整requirements.txt对应依赖包的版本号，然后继续尝试即可。一般情况下调整为提示所需范围的最新版本即可。

### 3.2 压缩

将ubuntu软件压缩打包。python所需依赖包可以不用压缩。

1. 进入"/var/cache/apt/"下。确保其下有"/var/cache/apt/archives"目录。
   ```shell
   cd /var/cache/apt/
   ```
2. 将"/var/cache/apt/archives"目录压缩。
   ```shell
   tar -czvf archives.tar.gz archives
   ```

### 3.3 拷贝到离线环境中

如题。

### 3.4 解压缩

对压缩的文件进行解压缩。

1. 进入所需要存放ubuntu软件的目录。
2. 解压缩。使用命令如下：
   ```shell
   tar -zxvf archives.tar.gz
   ```
3. 进入解压缩生成的当前路径下的archives文件夹
   ```shell
   cd archives
   ```

### 3.5 首先安装ubuntu的软件源（其中一定要包含pip的包）

安装所有ubuntu软件。注意在offline环境中安装了pip。

```shell
sudo dpkg -i *
```

### 3.5 安装python依赖包

将requirements.txt和python依赖包放在同一目录下。使用如下命令安装所有python依赖包：

```shell
pip install --no-index --find-links=[PythonDependenciesPath] -r requirements.txt
```
