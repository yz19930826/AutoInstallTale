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



if __name__ == '__main__':
    execShell('cd ..')
