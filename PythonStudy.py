#coding:utf-8
import math
import random
from pathlib import Path

what_he_does = ' plays'
his_instrument = ' guitar'
his_name = 'Robert Johnson'
artist_intro = his_name + what_he_does + his_instrument
print(artist_intro)

num = 1
string = '1'
#print(string + num) 会报错
#获取变量类型
print(type(num))
print(type(string))
#转换变量类型
num2 = int(string)
print(num + num2) #==> 2
string2 = str(num)
print(string + string2) #==> 11

#字符串除了可以相加，也可以相乘
words = 'words'
print(words + words)
print(words * 3)

word = 'a loooooong word'
num = 12
string = 'bang!'
total = string * (len(word) - num)  #等价于字符串 'bang!' * 4
print(total)

#字符串操作
#字符串 My Name is Mike
#索引为 0123456789
name = 'My Name is Mike'
#字符串长度
print(len(name)) #==> 15
#索引从 0 开始
print(name[0])  #==> M
#索引为负数表示从尾部开始
print(name[-1]) #==> e
print(name[-2]) #==> k
print(name[-3]) #==> i
print(name[-4]) #==> M
#从索引 11 开始，到 14 结束，不包含 14
print(name[11:14]) #==> Mik
#从索引 11 开始，到 14 结束，不包含 15
print(name[11:15]) #==> Mike
#输出索引 5 开始的字符串
print(name[5:]) #==> me is Mike
#输出从 0 开始到 5 结束的字符串，不包含 5
print(name[:5]) #==> My Na

word = 'friends'
find_the_evil_in_your_friends = word[0] + word[2:4] + word[-3:-1]
print(find_the_evil_in_your_friends) #==> fiend

#小场景：爬取的图片链接，下载后需要重新命名
url = 'https://ww1.site.cn/14d2e8ejw1exjogbxdxhj20ci0kuwex.jpg'
file_name = url[-10:]
print(file_name) #==> 0kuwex.jpg

#字符串替换
#只显示手机号码后四位，其他用'*'代替
phone_number = '188-0152-4569'
hiding_number = phone_number.replace(phone_number[:9], '*' * 9)
print(hiding_number) #==> *********4569

#字符串查找
search = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0007'
#在 num_a 中查找'168'，并返回num_a中'168'开始的索引下标，要是没找到返回-1
print(num_a.find(search)) #==> 5
print(num_b.find(search)) #==> 0
print(num_a.find('s')) #==> -1
print(search + ' is at ' + str(num_a.find(search) + 1) + ' to ' + str(num_a.find(search) + len(search)) + ' of num_a')
#==> 168 is at 6 to 8 of num_a
print(search + ' is at ' + str(num_b.find(search) + 1) + ' to ' + str(num_b.find(search) + len(search)) + ' of num_b')
#==> 168 is at 1 to 3 of num_b

#字符串格式化（相当于填空），使用方式
print('{} a word she can get what she {} for'.format('With', 'came'))
#==> With a word she can get what she came for
print('{preposition} a word she can get what she {verb} for'.format(preposition = 'with', verb = 'came'))
#==> With a word she can get what she came for
print('{0} a word she can get what she {1} for'.format('with', 'came'))
#==> With a word she can get what she came for

#字符串格式化应用，百度天气数据接口-获取城市信息
city = 'chengdu'
#输入函数 input('What is your city? ')
print('https://apistore.baidu.com/microservice/weather?citypinyin={}'.format(city))

#函数
#定义一个华氏度转换为摄氏度的函数
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return str(celsius) + '℃'

#调用函数
F2C = fahrenheit_to_celsius(105)
print(F2C) #==> 40.55555555555556℃

#定义一个重量转换函数，传入参数g，返回kg
def g_to_kg(g):
    return g / 1000

g2kg = g_to_kg(105)
print("105g = " + str(g2kg) + "kg")

#定义一个求直角三角形斜边长的函数，传入两条直角边长度，返回斜边长度
#可以使用幂运算符'**'
def right_triangle_third_side(a, b):
    return (a * a + b * b) ** 0.5

third_side = right_triangle_third_side(3, 4)
print("The right triangle third side\'s length is {0}".format(third_side))

#传递参数的方式
#定义一个计算梯形面积的函数
def trapezoid_area(base_up, base_down, height):
    return height * (base_up + base_down) / 2

#位置参数
trapezoid_1 = trapezoid_area(1, 2, 3)
print("The trapezoid_1 area is {}".format(trapezoid_1))
#关键词参数
trapezoid_2 = trapezoid_area(base_up=1, base_down=2, height=3)
print("The trapezoid_2 area is {}".format(trapezoid_2))
#改变关键词参数顺序也可以正常传入
trapezoid_3 = trapezoid_area(height=3, base_up=1, base_down=2)
print("The trapezoid_3 area is {}".format(trapezoid_3))
#逆序传入，混用位置参数和关键词参数传入，则会报错
#trapezoid_4 = trapezoid_area(height=3, base_down=2, 1)
#这样也会报错
# trapezoid_4 = trapezoid_area(base_up=1, base_down=2, 3)
#这样不会报错
trapezoid_4 = trapezoid_area(1, 2, height=3)
print("The trapezoid_4 area is {}".format(trapezoid_4))

#给形参设置默认参数
def trapezoid_area_default(base_up, base_down, height=3):
    return height * (base_up + base_down) / 2

# 不要用函数名当做变量，不然会将此函数重置
# trapezoid_area_default = trapezoid_area_default(1, 2)
trapezoid_5 = trapezoid_area_default(1, 2)
print("The trapezoid_5 area is {}".format(trapezoid_5))

#文件操作
def file_test():
    file = open('test.txt', 'w')
    file.write('Hello World!\n')
    file.close()
# file_test()

"""
    设计一个简易的敏感词过滤器
"""
#创建文本文件
def text_create(name, msg):
    workspace_path = 'E://Workspace/Python/PythonStudy/'
    full_path = workspace_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print('Done!')
#text_create('hello', 'Hello World!')

#过滤
def text_filter(word, censored_word = 'lame', changed_word = 'Awesome'):
    return word.replace(censored_word, changed_word)
print(text_filter('Python is lame!'))

#文件写入过滤
def text_censored_create(name, msg):
    clean_msg = text_filter(msg)
    text_create(name, clean_msg)
# text_censored_create('Try', 'lame!lame!lame!')

"""
    列表
"""
#创建列表
album = []
album = ['Black Star', 'David Bowie', 25, True]
#向列表中添加新的元素，自动添加到尾部
album.append('new song')
#打印列表的第一个元素和最后一个元素
print(album[0], album[-1]) #==> Black Star new song
print(album) #==> ['Black Star', 'David Bowie', 25, True, 'new song']

#判断归属关系：in, not in
#判断某个元素是否在列表中
print('归属关系判断：in, not in')
print('Black Star' in album) #==> True
print('Black Star' not in album) #==> False

#身份鉴别：is, not is
print('身份鉴别：is, not is')
the_Eddie = 'Eddie'
eddie_name = 'Eddie'
print(the_Eddie == eddie_name) #==> True
print(the_Eddie is eddie_name) #==> True

#可以使用bool()方法判断任意对象
#除了0，None 和所有空的序列与集合（列表、字典、集合）布尔值为False外，其他都为 True
print('bool()方法判断任意对象')
print(bool(0)) #==> False
print(bool([])) #==> False
print(bool('')) #==> False
print(bool(False)) #==> False
print(bool(None)) #==> False

#not, and, or
print('布尔运算：not, and, or')
print(not False) #==> True
print(1 < 3 and 2 < 5) #==> True
print(1 < 3 and 2 > 5) #==> False
print(1 < 3 or 2 > 5) #==> True
print(1 > 3 or 2 > 5) #==> False

#条件控制：if elif else
print('条件控制：if, elif, else')
#定义一个账户登录的函数
def account_login(password):
    if password == '12345':
        print('Login successfully!')
    else:
        print('Wrong password, Login failed!')

account_login('<PASSWORD>') #==>Wrong password, Login failed!
account_login('12345') #==>Login successfully!

#定义一个账户登录的函数，增加重置密码功能
#密码列表
password_list = ['*#*#', '12345']
def account_login_reset(password):
    correct_password = password == password_list[-1]
    reset_password = password == password_list[0]
    if correct_password:
        print('Login successfully!')
    elif reset_password:
        new_password = 'abcde'
        #在密码列表中追加新密码
        password_list.append(new_password)
        print('Your password has been reset.')
    else:
        print('Wrong password, Login failed!')

print('登录失败，重置密码：')
account_login_reset('<PASSWORD>') #==>Wrong password, Login failed!
account_login_reset('12345') #==>Login successfully!
account_login_reset('*#*#') #==>Your password has been reset.

"""
    for 循环
"""
print('for 循环')
for every_letter in 'Hello':
    print(every_letter)
"""
结果：
H
e
l
l
o
"""
#内置函数 range()
for num in range(1, 11): #不包含11，因此实际范围是1-10
    print(str(num) + ' + 1 = ', num + 1)

songs_list = ['Holy Diver', 'Thunderstruck', 'Rebel Rebel']
for song in songs_list:
    if song == 'Holy Diver':
        print(song, ' - Dio')
    elif song == 'Thunderstruck':
        print(song, ' - AC/DC')
    elif song == 'Rebel Rebel':
        print(song, ' - David Bowie')

#九九乘法口诀表
for i in range(1, 10):
    for j in range(1, 10):
        print('{} x {} = {}'.format(i, j, i * j))

#while 循环
print('while 循环：')
count = 0
while True:
    print('Repeat this line!')
    count += 1
    if count == 5:
        break

password_list_new = ['*#*#', '12345']
def account_login_new():
    tries = 3
    while tries > 0:
        password = input('Password: ')
        correct_password = password == password_list_new[-1]
        reset_password = password == password_list_new[0]

        if correct_password:
            print('Login successfully!')
        elif reset_password:
            new_password = input('New password: ')
            password_list_new.append(new_password)
            account_login_new()
            break
        else:
            print('Wrong password, Login failed!')
            tries -= 1
            print(tries, 'times left')
    else:
        print('Your account has been suspended!')

#account_login_new()

"""
    创建十个文本，以数字给它们命名
"""
def create_ten_text():
    #获取当前工作目录
    current_dir = Path.cwd()

    #在当前目录创建目标文件夹
    target_folder = current_dir / "create_ten_text"
    #parents=True 如果父目录不存在，则创建父目录；exist_ok=True，如果目标文件夹已存在，则直接使用，不会报错
    target_folder.mkdir(parents=True, exist_ok=True)

    #创建10个文本文件
    for i in range(1, 11):
        file_path = target_folder / f'text_{i}.txt'
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f'这是文件 {i} 的内容')
    print(f'已在当前目录创建文件夹：{target_folder}')
    print(f'已在 {target_folder} 创建10个文本文件')

# create_ten_text()

"""
    f-string
    Python 3.6引入的强大字符串格式化方法
"""
def f_string_test():
    name = "Alice"
    age = 30

    #直接嵌入表达式
    print(f"{name.upper()} is {age + 1} next year") #==>ALICE is 31 next year

    #调用函数和方法
    print(f"π 的值是 {math.pi:.7f}") #==>π 的值是 3.1415927

    #格式化选项
    price = 99.99
    print(f"价格：{price:.2f}元") #==>价格：99.99元

    date = (2025, 7, 11)
    print(f"日期：{date[0]}-{date[1]:02d}-{date[2]:02d}") #==>日期：2025-07-11

f_string_test()

#f-string 处理复杂对象
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person({self.name}, {self.age})"

p = Person("Alice", 30)
print(f"用户信息：{p}") #==>用户信息：Person(Alice, 30)

"""
    设计一个复利计算函数 invest()，它包含三个参数：amount（资金），rate（利率），time（投资时间）。
    输入每个参数后调用函数，应该返回每一年的资金总额。
"""
def invest(amount, rate, time):
    """
    计算复利投资每年的资金总额
    :param amount:初始投资金额
    :param rate:年利率（比如5%）
    :param time:投资年限
    :return: list 每年结束时的资金总额列表
    """
    #每年结束时的资金总额列表
    funds = []

    #本金
    print(f"principal amount: ${amount}")
    #利率
    print(f"principal rate: {rate}")
    #当前总额
    current_amount = amount
    for i in range(1, time + 1):
        current_amount = current_amount + current_amount * rate
        funds.append(current_amount)
        print(f"year {i}: ${current_amount:,.2f}")

    return funds

invest(10000, 0.05, 8)

def even_number(number):
    """
        打印number以内的偶数
    :return:
    """
    #传入的number不是数字
    if not isinstance(number, (int, float)):
        print(f"{number}不是数字")
        return

    #传入的number是浮点数，转为整数
    if isinstance(number, float):
        number = int(number)

    #0的情况
    if number == 0:
        print(f"{number}以内的偶数有：0")
    #正数
    elif number > 0:
        for i in range(0, number + 1, 2):
            print(f"{number}以内的偶数有：{i}")
    #负数
    else:
        for i in range(0, number - 1, -2):
            print(f"{number}以内的偶数有：{i}")
# even_number(-10)

"""
    综合练习：猜骰子大小
"""
def roll_dice(numbers=3, point_list=None):
    """获取三个骰子的点数"""
    print("<<<<<===== ROLL THE DICE! =====>>>>>")
    if point_list is None:
        point_list = []

    for i in range(0, numbers):
        point = random.randrange(1, 7)
        point_list.append(point)
    return point_list

def big_or_small(total):
    """定义大小"""
    is_small = 3 <= total <= 10
    is_big = 11 <= total <= 18
    if is_small:
        return "Small"
    elif is_big:
        return "Big"
    return None

def bet():
    """押注"""


def dice_game():
    """扔骰子猜大小游戏"""
    print("<<<<<===== GAME STARTS! =====>>>>>")
    user_choice = ['Big', 'Small']

    user_input = input("Big or Small:")
    if user_input in user_choice:
        #获取骰子点数
        point_list = roll_dice()
        dice_sum = sum(point_list)
        #骰子大小
        result = user_input == big_or_small(dice_sum)

        if result:
            print("The points are ", point_list, dice_sum, " point! You win!")
        else:
            print("The points are ", point_list, dice_sum, " point! You lose!")
    else:
        print("invalid input! Please try again!")
        dice_game()
dice_game()