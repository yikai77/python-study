what_he_does = " plays"
his_instrument = " guitar"
his_name = "Robert Johnson"
artist_intro = his_name + what_he_does + his_instrument
print(artist_intro)

num = 1
string = "1"
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
words = "words"
print(words + words)
print(words * 3)

word = "a loooooong word"
num = 12
string = "bang!"
total = string * (len(word) - num)  #等价于字符串 "bang!" * 4
print(total)

#字符串操作
#字符串 My Name is Mike
#索引为 0123456789
name = "My Name is Mike"
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
#从索引 11 开始，到 15 结束，不包含 15
print(name[11:15]) #==> Mike
#输出索引 5 开始的字符串
print(name[5:]) #==> me is Mike
#输出从 0 开始到 5 结束的字符串，不包含 5
print(name[:5]) #==> My Na

word = "friends"
find_the_evil_in_your_friends = word[0] + word[2:4] + word[-3:-1]
print(find_the_evil_in_your_friends) #==> fiend

#小场景：爬取的图片链接，下载后需要重新命名
url = "https://ww1.site.cn/14d2e8ejw1exjogbxdxhj20ci0kuwex.jpg"
file_name = url[-10:]
print(file_name) #==> 0kuwex.jpg

#字符串替换
#只显示手机号码后四位，其他用"*"代替
phone_number = "188-0152-4569"
hiding_number = phone_number.replace(phone_number[:9], "*" * 9)
print(hiding_number) #==> *********4569

#字符串查找
search = "168"
num_a = "1386-168-0006"
num_b = "1681-222-0007"
#在 num_a 中查找"168"，并返回num_a中"168"开始的索引下标，要是没找到返回-1
print(num_a.find(search)) #==> 5
print(num_b.find(search)) #==> 0
print(num_a.find("s")) #==> -1
print(search + " is at " + str(num_a.find(search) + 1) + " to " + str(num_a.find(search) + len(search)) + " of num_a")
#==> 168 is at 6 to 8 of num_a
print(search + " is at " + str(num_b.find(search) + 1) + " to " + str(num_b.find(search) + len(search)) + " of num_b")
#==> 168 is at 1 to 3 of num_b

#字符串格式化（相当于填空），使用方式
print("{} a word she can get what she {} for".format("With", "came"))
#==> With a word she can get what she came for
print("{preposition} a word she can get what she {verb} for".format(preposition = "with", verb = "came"))
#==> With a word she can get what she came for
print("{0} a word she can get what she {1} for".format("with", "came"))
#==> With a word she can get what she came for
#当前更常用更高效的用法
str1 = "with"
str2 = "came"
print(f"{str1} a word she can get what she {str2} for")
#==> With a word she can get what she came for

#字符串格式化应用，百度天气数据接口-获取城市信息
city = input("What is your city? Please input city pinyin:")
print(f"https://apistore.baidu.com/microservice/weather?citypinyin={city}")
