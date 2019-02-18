##python官网

https://www.python.org/
## 下载最新版
wget https://www.python.org/ftp/python/3.4.4/Python-3.4.4.tgz

## 下载完，不幸发现
``` shell
:~$ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.

```
不过这是正常的
接着
``` shell
--configure：避免对原有的Python产生影响，必须制定prefix。
 
timeloveboy@timeloveboy /usr/local/Python-3.4.4$ ./configure --prefix=/usr/local/python3.4.4
timeloveboy@timeloveboy /usr/local/Python-3.4.4$ make
timeloveboy@timeloveboy /usr/local/Python-3.4.4$ make install
```
建立软链接
``` shell
timeloveboy@timeloveboy /usr/local/Python-3.4.4$ sudo ln -s /usr/local/Python-3.4.4/python /bin/python3.4.4 
 ```
 退出python命令行命令
 CTRL+D
 
现在再输入
python3.4.4
即可进入
