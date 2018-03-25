## 写在前面的话

Tale博客手动安装已经介绍过了，相对来说简单，但是对技术不熟悉的朋友来说还是不怎么友好，所以抽时间写了个一键搭建的脚本。

至于Tale博客是什么，看下面文章的图集，有个感官上的认识即可：http://www.hellojava.club/java/66.html

## 搭建开始
首先你需要有一个VPS，如何使用和搭建SS（科学上网工具），看这篇文章：http://www.hellojava.club/shadowsocks/37.html

接下来就是需要在Xshell中输入以下命令：
```
wget --no-check-certificate -O tale.py https://raw.githubusercontent.com/yz19930826/AutoInstallTale/master/AutoInstallTale.py
chmod 777 tale.py
python tale.py
```
静静等待两分钟，出现下面的绿字则证明安装成功：
![image](http://upload-images.jianshu.io/upload_images/3883542-7fa26d3f7d7cb61d..jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

接着访问服务器的IP地址，如我的是:140.82.31.133,得到下面的结果：

![image](http://upload-images.jianshu.io/upload_images/3883542-c1926d90fb13b98a..jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

结束，就这么简单~