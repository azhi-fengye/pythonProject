import pymysql


class Mysql_Operation:
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host='localhost',  # IP，MySQL数据库服务器IP地址
                port=3306,  # 端口，默认3306，可以不输入
                user='root',  # 数据库用户名
                password='root',  # 数据库登录密码
                charset='utf8'  # 字符集，注意不是utf-8
            )
            self.cursor = self.conn.cursor()
        except pymysql.err.Error as e:  # as 和except组合使用，将捕获到的异常对象赋值给e
            print('连接数据库失败{}'.format(e))
        else:
            print('连接数据库成功')

    def create_DataBase(self, database_name):
        create_base = 'create database ' + database_name
        try:
            self.cursor.execute(create_base)
        except pymysql.err.ProgrammingError as e:
            print(repr(e))
        else:
            print('创建数据库成功：{}'.format(database_name))

    def use_DataBases(self, databases_name):
        choice_databases = 'use ' + databases_name
        try:
            self.cursor.execute(choice_databases)
        except pymysql.err.Error as e:
            print(repr(e))
            databases_name = input('没有找到{}数据库，请重新输入：'.format(databases_name))
            self.use_DataBases(databases_name)
        else:
            print('连接数据库{}成功'.format(databases_name))

    def create_DataTable(self, table_name, *args):
        args = str(args)
        args = list(args)
        args.pop(-2)
        str_args = ''.join(args)
        str_args = str_args.replace('\'', '').lstrip('(').rstrip(')')
        create_table = 'create table ' + table_name + ' ' + '(id int unsigned not null  auto_increment PRIMARY KEY,' + str_args + '));'
        try:
            self.cursor.execute(create_table)
        except pymysql.err.Error as e:
            print(create_table)
            print('创建数据表失败')
            print(repr(e))
            table_name = input('请重新输入您想要创建的数据表名：')
            args = input('请重新输入您想要创建的数据库表里的字段和字段类型：')
            self.create_DataTable(table_name, args)
        else:
            print('创建数据表成功')

    def change_Table(self, change_type, ):
        pass

    def show_BasesTable(self):
        str_ShowDataBases = 'show tables'
        self.cursor.execute(str_ShowDataBases)
        print(self.cursor.fetchone(), 'haha')
        for i in self.cursor:
            pass

    # 创建数据库
    # Mysql_new.create_database(input('创建数据库:'))

    # 创建数据库表
    # Mysql_new.create_Datatable(input('请输入您想要创建的数据表名'), input(
    #     '输入您想要创建的数据表的字段名和字段类型（请以name varchar(25),age int这样为模板）'))  # 'name varchar(25),age int,ce int'

    #


if __name__ == '__main__':
    # 创建一个操作数据库的实例
    Mysql_new = Mysql_Operation()
    # 选择数据库
    Mysql_new.use_DataBases(input('请输入您需要操作的数据库'))

    Mysql_new.show_BasesTable()
