import pymysql


class Mysql_Operation:
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host='localhost',  # IP，MySQL数据库服务器IP地址
                port=3306,  # 端口，默认3306，可以不输入
                user='root',  # 数据库用户名
                password='root',  # 数据库登录密码
                database='taoxu',  # 要连接的数据库
                charset='utf8'  # 字符集，注意不是utf-8
            )
            self.cursor = self.conn.cursor()
        except pymysql.err.OperationalError as e:  # as 和except组合使用，将捕获到的异常对象赋值给e
            print('连接数据库失败{}'.format(e))
        else:
            print('连接数据库成功')

    def create_database(self, database_name):
        create_base = 'create database ' + database_name
        try:
            self.cursor.execute(create_base)
        except pymysql.err.ProgrammingError as e:
            print(repr(e))
        else:
            print('创建数据库成功：{}'.format(database_name))

    def create_datatable(self, table_name, *args):
        print(args)
        str_args = list(args)
        print(str_args)
        str_args = str(str_args)
        print(str_args)
        # str_args.pop(-2)
        # str_args=''.join(str_args)
        # print(str_args)
        # create_table = 'create table' + table_name+' '+ str_args
        # print(create_table)
        # self.cursor.execute(create_table)


# 创建一个操作数据库的实例
Mysql_new = Mysql_Operation()

# Mysql_new.create_database(input('创建数据库:'))
Mysql_new.create_datatable('haolaji', 'name varchar(25),age int(5),ce int(5)')
