#函数学习

#定义一个华氏度转换为摄氏度的函数
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return str(celsius) + "℃"



if __name__ == "__main__":
    F2C = fahrenheit_to_celsius(105)
    print(f"105华氏度 = {F2C}")