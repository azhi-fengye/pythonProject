import pymysql

# 打开数据库连接
connection = pymysql.connect(
    host='localhost',  # IP，MySQL数据库服务器IP地址
    port=3306,  # 端口，默认3306，可以不输入
    user='root',  # 数据库用户名
    password='root',  # 数据库登录密码
    database='taoxu',  # 要连接的数据库
    charset='utf8'  # 字符集，注意不是'utf-8'
)

# 使用cursor()方法创建一个游标对象cursor
cursor = connection.cursor()

# 查询语句
select_sql = "SELECT * FROM student_text"

# fetchone()方法
try:
    # 执行sql语句
    cursor.execute(select_sql)
    result_one = cursor.fetchone()
    print(result_one)
except:
    print('fetchone获取数据失败')
