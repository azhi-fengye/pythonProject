import pymysql
import random

file_sead = open('name.txt', 'r', encoding='utf8')
school_major_all = ['信息工程系', '海洋工程系', '机电工程系', '经济管理系', '艺术与设计系', '外语外贸系', '人文社科系']
name_all = file_sead.read().split(',')
age_all = [18, 19, 20, 21]
file_sead.close()

# 连接mysql；失败返回连接数据库失败，成功返回输出连接数据库成功。
try:
    # 连接mysql的方法 connect('ip','user','password','dbname')
    connection = pymysql.connect(
        host='localhost',  # IP，MySQL数据库服务器IP地址
        port=3306,  # 端口，默认3306，可以不输入
        user='root',  # 数据库用户名
        password='root',  # 数据库登录密码
        database='taoxu',  # 要连接的数据库
        charset='utf8'  # 字符集，注意不是'utf-8
    )
except:
    print('连接数据库失败')
else:
    print('连接数据库成功')

for i in range(3001):
    name = random.choice(name_all)
    title_id = i
    student_id = 2018328100 + i
    age = random.choice(age_all)
    major = random.choice(school_major_all)
    in_date = '2018年9月1日'
