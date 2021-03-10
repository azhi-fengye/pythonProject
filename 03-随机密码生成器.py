import random
import string

statiu_cookie = string.ascii_letters + string.digits
'''
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
string.ascii_letters:小写字母(string.ascii_lowercase)和大写字母(string.ascii_uppercase)常量的连接串
string.digits:数字0到9的字符串'0123456789'
'''

while True:
    try:
        passlen = int(input('请输入你需要的密码长度'))
    except ValueError:
        print('您输入了一个非数字，再见！')
        break
    else:
        if passlen <= 62:

            cpu_cookie = ''.join(random.sample(statiu_cookie, passlen))

            print(cpu_cookie, '')
        else:
            print('您输入的范围有误')
