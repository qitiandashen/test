# python创建文件夹和TXT文件，删除TXT文件和删除文件夹
'''需求：
1、先在E盘创建一个TEST文件夹。
2、在TEST文件夹内创建一个TXT文本文件并写入内容“Hello world!”
3、删除TEST文件夹内的TXT文件
4、删除路径TEST文件目录'''
import os,stat,time
dirPath='E:\\study_dir\\'
filename='a.txt'
def createfile():
    if (os.path.exists(dirPath)):
        print('目录'+dirPath+'已经存在')
    else:
        os.mkdir(dirPath)
        print('创建目录'+dirPath)
    file_path = dirPath + filename
    print("file_path： " + file_path)
    with open(file_path,mode='w+',encoding='utf-8')as f:
        f.write('hello world')


def deleteFile():
    print('移除前' + dirPath + '目录下有文件：%s' % os.listdir(dirPath))
    # 判断文件是否存在
    if (os.path.exists(dirPath + filename)):
        os.remove(dirPath + filename)
        print('移除后' + dirPath + '目录下有文件：%s' % os.listdir(dirPath))
    else:
        print("要删除的文件不存在！")
def deletePath():
    if (os.path.exists(dirPath)):
        os.rmdir(dirPath)  # 删除目录
        print('移除' + dirPath + '目录')
    else:
        print("要删除的路径不存在！")

print("开始执行----------------------------------------------------------------------------------------")
createfile()
time.sleep(8)# 8 秒后删除TXT文件
deleteFile()
time.sleep(8)# 8 秒后删除路径TEST
deletePath()
print("结束执行----------------------------------------------------------------------------------------")


