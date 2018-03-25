# coding:utf-8
# 测试文件读写
import os



# 将指定的内容写入文件
def editFileContent(filepath,content):
    #判断文件是否存在
    fileexists = os.path.exists(filepath)
    if(fileexists):
        #打开文件
        file = open(filepath,'a+')
        #将内容写入文件
        file.write(content)
        #关闭
        file.close()


# 判断文件内容是否已经存在在文件中
def isContentInFile(filepath,content):
    fileexists = os.path.exists(filepath)
    if(fileexists):
        #open file
        file = open(filepath)
        data = file.read()
        if data.index(content)>-1:
            return False
        else:
            return True


def get_ip():
    #注意外围使用双引号而非单引号,并且假设默认是第一个网卡,特殊环境请适当修改代码
    out = os.popen("ifconfig | grep 'inet addr:' | grep -v '127.0.0.1' | cut -d: -f2 | awk '{print $1}' | head -1").read()
    print out

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

if __name__ == '__main__':
    get_ip()
    print("\033[1;34;47m恭喜您，搭建完成，访问:！\033[0m")
    print("\033[1;34;40m想了解更多，请访问：www.hellojava.club\033[0m")

