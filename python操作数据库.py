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

# 创建数据库
# cursor.execute('create database mydatabese')

# 创建表
# cursor.execute("CREATE TABLE customers (name varchar(255),address varchar(255))")

# 修改表操作
# cursor.execute('alter table customers add id int primary key auto_increment')
# 修改costomers表 添加id字段 类型为int 主键 自增

# 查询并打印数据库中的所有表
# cursor.execute('show tables')
# for table in cursor:
#     print(table)

# 插入数据
sql = 'insert into student_text(id,student_id,name,age,in_date,out_date,major) values (%(id)s,%(student_id)s,%(name)s,%(age)s,%(in_date)s,%(out_date)s,%(major)s)'
sql_values = {
    'id': 3001,
    'student_id': 2018331101,
    'name': '憨憨梨',
    'age': 18,
    'in_date': '2018-9-1',
    'out_date': '2021-6-30',
    'major': '信息工程系'
}  # 以字典的形式填入数据
cursor.execute(sql, sql_values)
cursor.connection.commit()  # 请记得添加这句提交代码
