#遍历字典
'''users={"liukang":"python","zhangsan":"java"}
friend=["lizhong","zhangsan"]
for name in users.keys():
    print(name.title())
    if name in friend:
        print('hello '+name.title())
    else:
        print('you must study')'''
# 按顺序遍历字典,使用sorted函数
'''users={"liukang":"python","zhangsan":"java","andlabay":"c"}
friend=["lizhong","zhangsan"]
for name in sorted(users.keys()) :
    print(name.title())
    if name in friend:
        print('hello '+name.title())
    else:
        print('you must study')'''
'''# 获取
users={"liukang":"python","zhangsan":"java","andlabay":"c","babab":"python"}
for v in users.values():
    print('\tyou are study langyage:'+v)'''
'''# 有时候为了获取值，把重复的值去掉，要使用set集合
users={"liukang":"python","zhangsan":"java","andlabay":"c","babab":"python"}
lan=[]
for v in set(users.values()):
    lan.append(v)
    print('you are learn language:'+v)
    print(lan)
print(lan)'''
''''# 列表的嵌套，列表中嵌套字典
alia={'zhangsan':'lisi','wangwu':'qinhghua'}
bala={"love":"quity","much":"very"}
calc={"big":"fix"}
lists=[alia,bala,calc]
for v in lists:
    print(v)'''
# 创建30个外星人列表
'''aliea=[]
for aliea_number in range(30):
    new_aliea={"color":"green","point":5,"speed":"slow"}
    aliea.append(new_aliea)
# 修改前三个人身份
for people in aliea[:3]:
    if people['color']=="green":
        people["color"]="yellow"
        people['speed']='medium'
        people['point']=10
    elif people['color']=="yellow":
        people["color"] = "red"
        people['speed'] = 'fast'
        people['point'] = 15
#如果黄色更快
for people in aliea[:6]:
    if people['color']=="yellow":
        people["color"] = "red"
        people['speed'] = 'fast'
        people['point'] = 15


# 显示前五个
for people in aliea[:5]:
    print(people)
print('----------')
print("total number of aliea:"+str(len(aliea)))'''
# 字典中存储列表
# 存储所点披萨信息
'''pizza={
    'crust':'thick',
    'topping':['mushroom','apple'],
}
# 概述所点的披萨
print('you order a '+pizza['crust']+'with the follwoing topping:')
for topping in pizza['topping']:
    print('\t'+topping)'''
# 学习不同语言
'''love_languages={
    'liukang':['java','python'],
    'zhangsan':['c'],
    'lisi':['ruby','go'],
    'wangwu':['go','shell'],

}
for name,languages in love_languages.items():
    print('\t'+name.title()+' is love_language:')
    for language in languages:
        print('\t'+language.title())'''
# input函数的用法
'''name=input('please enter your name :')
print('hello ,'+name)'''
'''age =input('how old are you:')
age=int(age)
if age>=18:'''
# 求模运算符
'''z=5%3
print(z)'''
# 判断一个函数是奇数还是偶数
'''number=input('please enter a number:')
number=int(number)
if number%2==0:
    print('number is odd')
else:
    print('number is even')'''
# while的使用
'''number=0
i=0
while i<=5:

    number=number+i
    i+=1
    print(number)
#使用sum函数，直接就可以直接计算100以内的加法
sum=sum(range(6))
print(sum)'''
# while 循环的使用
'''prompt='\n tell me something.and i want repeat to you :'
prompt+='\n what are you nong sha ne，enter quit over :'
active=True
while active:
    message=input(prompt)
    if message =='quit':
        break'''
# while 循环的continue
'''number=0
while number<20:
    number+=1
    if number %2==0:
        continue
    print(number)'''
# 使用while循环来处理列表和字典--在列表之间移动元素
'''user1=['liukang','zhangsan','lisi']
user2=[]
while user1:
    user3=user1.pop()
    print('you verifed:'+user3.title())
    user2.append(user3)
# 显示已经所有验证的姓名
print('\n the following user have been confirm： ')
for confire in user2:
    if confire=='liukang':
        break
    print(confire)
'''
# 删除包括特定值得所有列表元素
'''pets=['dog','cat','fish','rabbit','dog']
while 'dog'in pets:
    pets.remove('dog')
print(pets)'''
# 玩下函数
'''def build_person(first_name,last_name,age=''):
    person={'first_name':first_name,'last_name':last_name}
    if age:
        person['age']=age
    return person
hero=build_person('liukang','dugu',age=28)
print(hero)'''
# 结合使用函数组合while循环
'''def get_name(first_name,last_name):
    full_name=first_name+''+last_name
    return full_name
while True:
    print('\nplease tell me your name:')
    print('\nplease enter quit stop')
    f_name=input('first_name:')
    if f_name=='quit':
        break
    l_name=input('last_name:')
    if l_name=='quit':
        break
    heros=get_name(f_name,l_name)
    print('hello,'+heros+'!')'''
# 函数中传递列表
'''def greet(zhangsan):
    for name in zhangsan:
        msg='hello'+' '+name.title()
        print(msg)
zhangsan=['liukang','zhangsan','lisi']
greet(zhangsan)'''
# 在函数中修改列表：
'''before_desgin=['zhangsab','lisi','wangwu']
after=[]
while before_desgin:
    current_desgin=before_desgin.pop()
    print('now desin'+current_desgin)
    after.append(current_desgin)
# 显示最后新的函数
print('new desgin:')
for new in after:
    print(new)'''
# 利用函数思维
'''def print_model(before,after):
    while before:
        current=before.pop()
        print('old now'+current)
        after.append(current)
def show(after):
    print('new ')
    for new in after:
        print(new)
before=['lisi','zhangsan','wangwu']
after=[]
print_model(before,after)
show(after)
'''
# 传递任意数量的实参
'''def make_pizza(*toppins):
# 打印客户的账号
    print('\nmake a pizza following tops:')
    for toping in toppins:
        print('-'+ toping)
# 不管使用多少个值，这个参数都是可以用的；
make_pizza('nut')
make_pizza('zhansan','lisi')'''
# 结合使用位置实参和任意数字实参
'''表示pizza的大小实参'''
'''def make_pizza(size,*toppins):
    print('\n make a pizza'+ str(size) +' ' 'with following:')
    for toping in toppins:
        print('-' + toping)
make_pizza(17,'nut')
make_pizza(19,'liukang','zhangsan')'''
# 任意关键字实参是用一个*，任意数量实参用一个*
# 使用任意数量的关键字实参，有些时候，需要接受任意实参，但是不知道传递什么样信息，这个时候就需要
'''def make_name(first,last,**user_info):
    profile={}
    profile['first']=first
    profile['last']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile
user_profile=make_name('zheng xiamin','liukang',love='you',you='love me')
print(user_profile)'''

# 第9章 类-创建和使用类
# 创建dog类
'''class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(self.name.title()+"is now sitting")
    def roll_over(self):
        print(self.name.title()+'is now rolling'+ str(self.age))
my_dog=Dog('white',9)
# print('my dog name is:'+my_dog.name.title())
# print('my dog age is:'+str(my_dog.age))
my_dog.sit()
my_dog.roll_over()
# 此时可以创建多个实例
your_dog=Dog('smith',8)
your_dog.sit()
your_dog.roll_over()'''
# 使用类和实例--创建一个实例
'''class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.mile=0
    def get_detal(self):
        full_name=str(self.year)+' '+self.model+' '+self.make
        return full_name.title()
    def read_mile(self,mile):
        self.read_mile +=mile

my_new_car=Car('BWM','730li',2018)
print(my_new_car.get_detal())

my_new_car.read_mile(99)'''
# 继承-子类的方法
'''class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.oldmeter_reading=0
    def get_descript(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def reading_oldmeter(self):
        print('this car is :'+str(self.oldmeter_reading)+'miles on it')
    def update_oldmeter(self,km):
        if km>=self.oldmeter_reading:
            self.oldmeter_reading=km
        else:
            print('you can not roll back an oldmeter')
    def add_oldmeter(self,m):
        self.oldmeter_reading+=m
class Elect(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_zize=70
    def batteryy_zize(self):
        print('this is battery is :'+str(self.battery_zize))
my_telsa=Elect('TESLA','MODEL',2019)
print(my_telsa.get_descript())
my_telsa.batteryy_zize()'''
# 文件和异常
'''with open ('E:\orderNum.txt')as f:
    cc=f.readlines()
for line in cc:
    print(line.rstrip())'''
# 使用本地存储数据，编写一个登陆，登陆次数限制三次
'''username = input('请输入您需要注册的用户名：')
password = input('请输入您的密码：')
with open('E:\list_of_info.txt',mode='w',encoding='utf-8') as f:
    f.write('{}\n{}'.format(username,password))
list_data = []
i = 1
while i <= 3:
    usn = input('请输入您的用户名：')
    psd = input('请输入您的密码：')
    with open('E:\list_of_info.txt', mode='r+', encoding='utf-8') as f1:
        for line in f1:
            list_data.append(line)
            # print(lilst_data)
    if usn == list_data[0].rstrip() and psd == list_data[1].strip():
        print('登录成功')
        break
    else:
        print('请重新登录！')
        i+=1
        if i==4:
            print('你是一个傻逼，自己的密码都忘记了,账户已经被锁')
'''
# 编写一个存入本地的登录密码校验
'''username=input('请注册你的账户：')
password=input('请设置自己的密码：')
with open ('E:\python.txt',mode='w+',encoding='utf-8')as f:
    f.write('{}\n{}'.format(username,password))
list_data=[]
i=1
while i<=3:
    usa=input('请输入你的账户：')
    pas=input('请输入你的密码：')
    with open('E:\python.txt',mode='r+',encoding='utf=8')as f1:
        for line in f1:
            list_data.append(line)
    if usa==list_data[0].rstrip() and pas==list_data[1].rstrip():
        print('登录成功')
        break
    else:
        print('请输入正确账号或密码')
        i+=1
        if i==4:
            print('你像连博文一样SB，密码都记不住')
'''
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

















