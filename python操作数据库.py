import pymysql

# 连接数据库
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

sql_values = {  # 以字典的形式填入数据
    'id': 3003,
    'student_id': 2018331101,
    'name': '\'测试\'',  # 因为在数据库语句中字符串需要添加单引号或者双引号
    'age': 18,
    'in_date': '\'2018-9-1\'',
    'out_date': '\'2021-6-30\'',
    'major': '\'信息工程系\''
}
# 创建数据库
cursor.execute('create database mydatabese1')
# 创建表
# cursor.execute("CREATE TABLE customers (name varchar(255),address varchar(255))")

# 修改表操作
# cursor.execute('alter table customers add id int primary key auto_increment')
# 修改costomers表 添加id字段 类型为int 主键 自增

# 查询并打印数据库中的所有表
# cursor.execute('show tables')
# for table in cursor:
#     print(table)


# 查询数据
# select_sql = 'select student_id,name,age,major from student_text where name=\'海妍\';'  # 根据学生姓名查询数据
# cursor.execute(select_sql)  # 返回值为受影响的行数，如下：
## num=cursorl.execute(sql)
## print(num)结果为num=8

# r_all = cursor.fetchall()  # 取出全部查询结果
# r_one = cursor.fetchone()  # 取出一行查询结果。从第一行开始取
# r_many = cursor.fetchmany(size=2)  # 取出其中几行查询结果
## 如fetchall(),fetchmany(),fetchone()同时作用于同一个查询时，每个方法执行开头是上一个方法执行的结尾,例如第一句fetchall没有注释掉 后面俩句获取到的都是none
# print(r_all)  # 输出的数据类型为元组

## 插入数据（）
# insert_sql = 'insert into student_text(id,student_id,name,age,in_date,out_date,major) values ({id},{student_id}, {name}, {age}, {in_date}, {out_date}, {major}) '.format(
#     **sql_values)
# # on duplicate key updatestudent_id = {student_id}, name = {name}, age = {age}, in_date = {in_date},out_date={out_date},major={major}
# try:
#     cursor.execute(insert_sql)
# except:
#     print('提交失败,数据库已有该数据')
#     connection.rollback()
# else:
#     connection.commit()
#     print('提交成功')

# # 删除数据
# delete_sql = 'DELETE FROM student_text where student_id=2018331097;'
# # 如果没有指定 WHERE 子句，MySQL 表中的所有记录将被删除。
# cursor.execute(delete_sql)
# connection.commit()

# # 更新数据
# update_sql = 'UPDATE student_text set name=\'梨梨\',age=20 where id=2996'
# # 不使用 WHERE 子句将数据表的全部数据进行更新，所以要慎重。
# cursor.execute(update_sql)
# connection.commit()
'''
上面的实例中，使用的均是普通游标，返回结果为元组：查看起来不太方便，我们可以通过游标类型来控制数据返回类型
定义游标类型：在connect()中通过 “cursorclass=pymysql.cursors.DictCursor” 来定义

不缓存游标的用法：
用途：用于返回大量数据，查询，或慢速网络连接到远程服务器不将每行数据复制到缓冲区,根据需要获取行。客户端内存使用少在慢速网络上或结果集非常大时行返回速度快
限制:MySQL协议不支持返回总行数,判断有多少行唯一方法是选代返回的每一行。
目前无法向后滚动,因为只有当前行保存在内存中。
'''
