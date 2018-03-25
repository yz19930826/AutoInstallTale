## 写在前面的话

Tale博客手动安装已经介绍过了，相对来说简单，但是对不懂技术的朋友来说还是不怎么友好，所以抽时间写了个一键搭建的脚本。

至于Tale博客是什么，看下面文章的图集，有个感官上的认识即可：http://www.hellojava.club/java/66.html

## 搭建开始

```
wget --no-check-certificate -O tale.py https://raw.githubusercontent.com/yz19930826/AutoInstallTale/master/AutoInstallTale.py
chmod 777 tale.py
python tale.py
```
静静等待两分钟，等到下面的结果说明搭建成功:

![](http://p1hy9syru.bkt.clouddn.com/18-3-25/4149798.jpg)

接着访问服务器的IP地址，如我的是:140.82.31.133,得到下面的结果：

![](http://p1hy9syru.bkt.clouddn.com/18-3-25/60771070.jpg)

结束，就这么简单~