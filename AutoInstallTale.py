# coding:utf-8
import os
import urllib
import urllib2
import tarfile
import sys
import math
import zipfile

# JDK下载路径
JDK_URL = 'http://p1hy9syru.bkt.clouddn.com/jdk-8u151-linux-x64.tar.gz'
# JAVA_Home地址
JAVA_HOME = '/usr/local/java/'
#T TALE_HOME
TALE_HOME = '/usr/local/tale/'
# tale下载路径
TALE_URL = 'http://static.biezhi.me/tale-least.zip'

# 软件下载地址
SOFTWARE_PATH = "/usr/local/software/"

# profile内容
CONTENTSCHANGE = ''' export JAVA_HOME='''
CONTENTS = '''
        export JRE_HOME=${JAVA_HOME}/jre
        export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
        export PATH=${JAVA_HOME}/bin:$PATH
'''


# 获取当前路径
def getPwd():
    pwd = os.getcwd()
    print '当前路径：' + pwd
    return pwd


# 根据url下载文件
def downFile(url):
    # 判断文件是否存在
    filename = getFilename(url)
    fileexit = os.path.isfile(filename)
    if fileexit:
        print filename + '下载完毕！'
        return

    # 下载文件
    print '正在下载 ' + url + '...'
    f = urllib2.urlopen(url)
    data = f.read()

    with open(filename, "wb") as code:
        code.write(data)
    print '下载完成...'


# 获取url中的 文件名称
def getFilename(url):
    if not url:
        print '获取文件名称失败'
        return -1
    else:
        filename = url[url.rindex("/") + 1:]
        print '获取下载的文件名：' + filename
        return url[url.rindex("/") + 1:]


# 根据路径创建文件夹
def mkdir(path):
    dexit = os.path.exists(path)
    if dexit:
        print path + ' 已经存在!'
        return
    print '创建 ' + path + ' 文件夹'
    if path:
        os.mkdir(path)


# 文件下载进度条版
def downFileProcess(url, filepath):
    # 判断文件是否存在
    filename = getFilename(url)
    #若文件夹不存在
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    fileLocation = filepath + filename
    fileExist = os.path.isfile(fileLocation)
    if fileExist:
        print filename + '下载完毕！'
        return
    # 下载文件
    print '正在下载 ' + filename + '...'
    urllib.urlretrieve(url, fileLocation, reporthook=processBar)


# 回调函数
def processBar(transferedBlock, blockSize, allSize):
    # # 共多少个块
    allblockCount = allSize / blockSize
    # # 当前传输占的比例
    # proportion = (float(transferedBlock)/float(allblockCount))*100
    # if proportion>100:
    #     proportion = 100
    # # print '%4.2f %% ' % proportion
    # tag = "▋"
    # print int(proportion)*tag
    result = float(transferedBlock) / float(allblockCount);
    if (result > 1):
        return
    percent = '{:.2%}'.format(result)

    sys.stdout.write('\r')
    sys.stdout.write('[%-50s] %s' % ('=' * int(math.floor(transferedBlock * 50 / allblockCount)), percent))
    sys.stdout.flush()
    if transferedBlock == allblockCount:
        sys.stdout.write('\n')


# 解压tar.gz文件
def tarD(filepath, path):
    print '正在解压' + filepath + "文件，请耐心等待..."
    tar = tarfile.open(filepath)
    names = tar.getnames()
    folderName = ''
    i = 1;
    for name in names:
        print name
        tar.extract(name, path=path)
        # tar.close()
    print '解压' + filepath + "完成，关闭流~";
    tar.close()
    return names[0]


# 将字符串写入文件
def writeToFile(filename, contents):
    file = open(filename, 'a+')
    if file:
        file.write(contents)
    else:
        print '将' + contents + '写入' + filename + '失败'
        return


# 解压zip
def unzip_file(zipfilename, unziptodir):
    if not os.path.exists(unziptodir): os.mkdir(unziptodir, 0777)
    zfobj = zipfile.ZipFile(zipfilename)
    nameList = zfobj.namelist()
    for name in nameList:
        name = name.replace('\\', '/')

        if name.endswith('/'):
            if not os.path.exists(os.path.join(unziptodir, name)):
                os.mkdir(os.path.join(unziptodir, name))
            else:
                print zipfilename + '已解压'
                return nameList[0][0:nameList[0].index("/")];


        else:
            ext_filename = os.path.join(unziptodir, name)
            ext_dir = os.path.dirname(ext_filename)
            if not os.path.exists(ext_dir): os.mkdir(ext_dir, 0777)
            outfile = open(ext_filename, 'wb')
            outfile.write(zfobj.read(name))
            outfile.close()
    return nameList[0][0:nameList[0].index("/")]


# 将指定的内容写入文件
def editFileContent(filepath, content):
    # 打开文件
    file = open(filepath, 'a+')
    # 将内容写入文件
    file.write(content)
    # 关闭
    file.close()


# 判断文件内容是否已经存在在文件中
# filepath:文件路径
# content :需要判断的内容
# 若文本内容存在当前文件中，返回true，否则返回false
def isContentInFile(filepath, content):
    fileexists = os.path.exists(filepath)
    if (fileexists):
        # open file
        file = open(filepath)
        data = file.read()
        file.close()
        # 如果内容已经存在文件中，返回false
        if content in data:
            print content + '已经存在于：' + filepath
            return True
        else:
            return False
    return False


# 执行shell命令
def execShell(cmd):
    result = os.popen(cmd)
    print result.readlines()


# 启动程序
def start(processpath):
    print '启动：' + processpath
    file = open(processpath)
    file.close()


if __name__ == '__main__':
    print '开始搭建tale博客，请耐心等待...'
    # 获取当前路径
    pwd = getPwd()
    # 下载JDK
    downFileProcess(JDK_URL, SOFTWARE_PATH);
    # 根据URL获取文件名
    JdkTarFile = getFilename(JDK_URL)
    # 解压JDK
    folderName = tarD(SOFTWARE_PATH + JdkTarFile, JAVA_HOME)
    # 配置环境变量
    if not isContentInFile('/etc/profile', CONTENTS):
        # 拼接环境变量
        env = JAVA_HOME + folderName
        editFileContent('/etc/profile', CONTENTSCHANGE + env + '\n' + CONTENTS)
    # 下载tale.zip
    downFileProcess(TALE_URL,SOFTWARE_PATH)
    #获取下载的文件名
    taleName = getFilename(TALE_URL)
    #解压tale.zip
    taleFolderName = unzip_file(SOFTWARE_PATH+taleName,TALE_HOME)
    os.chdir(TALE_HOME+taleFolderName)
    result = execShell("./tale-cli start")
    for res in result:
        print res

    #配置防火墙
    execShell('systemctl stop firewalld.service')


    # foldername = tarD('jdk-8u151-linux-x64.tar.gz', getPwd())
    # print foldername
