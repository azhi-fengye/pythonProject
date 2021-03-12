import random

import pymysql

file_sead = open('name.txt', 'r', encoding='utf8')
school_major_all = ['信息工程系', '海洋工程系', '机电工程系', '经济管理系', '艺术与设计系', '外语外贸系', '人文社科系']
name_all = file_sead.read().split(',')
age_all = [18, 19, 20, 21]
file_sead.close()

# 连接mysql；失败返回连接数据库失败，成功返回输出连接数据库成功。

# 连接mysql的方法 connect('ip','user','password','dbname')
connection = pymysql.connect(
    host='localhost',  # IP，MySQL数据库服务器IP地址
    port=3306,  # 端口，默认3306，可以不输入
    user='root',  # 数据库用户名
    password='root',  # 数据库登录密码
    database='taoxu',  # 要连接的数据库
    charset='utf8'  # 字符集，注意不是utf-8

)
# 使用cursor()方法创建一个游标对象cursor
cursor = connection.cursor()

for i in range(1, 3000):
    student_id = 2018328100 + i
    name = random.choice(name_all)
    age = random.choice(age_all)
    in_date = '2018-9-1'
    out_date = '2021-6-30'
    major = random.choice(school_major_all)  # 随机系别
    insert_sql = 'insert into student_text(id,student_id,name,age,in_date,out_date,major) values ({},{},\'{}\',{},\'{}\',\'{}\',\'{}\');'.format(
        i, student_id, name, age, in_date, out_date, major)
    cursor.execute(insert_sql)
    cursor.connection.commit()

select_sql = 'select * from student_text'
cursor.execute(select_sql)
result_one = cursor.fetchone()
result_two = cursor.fetchone()
print(result_one)
print(result_two)
