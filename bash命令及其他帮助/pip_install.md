使用 wand 这个工具。
首先安装OSX下的包管理工具 Homebrew ，安装命令就是其主页下方Install Homebrew的一行命令。然后安装python和wand需要的几个工具:
```
$ brew install python imagemagick ghostscript wget
```
用brew安装的python应该比Mac自带的python新，写这篇文章时安的python是2.7.8_2。这时候电脑上会有两个python，用brew link命令来确保使用新的python：
```
$ brew link python
$ python -V
```
用brew missing查看还缺了什么东西，然后都装上:
```
$ brew missing
```
然后安装python的包管理工具pip，根据 其主页的说明 :
```
$ wget https://bootstrap.pypa.io/get-pip.py
$ python get-pip.py
$ rm -f get-pip.py
```
有了pip, 就可以很容易地安装wand了:
```
$ pip install wand
```