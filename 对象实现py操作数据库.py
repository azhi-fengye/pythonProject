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
            print('连接数据库后台失败{}'.format(e))
        else:
            print('连接数据库后台成功')

    def show_DataBases(self):
        str_ShowDataBases = 'show databases'
        self.cursor.execute(str_ShowDataBases)
        print('您拥有的数据库为')
        for databases_name in self.cursor:
            print(databases_name)

    def create_DataBases(self, database_name):
        create_base = 'create database ' + database_name
        try:
            self.cursor.execute(create_base)
        except pymysql.err.ProgrammingError as e:
            print(repr(e))
        else:
            print('创建数据库成功：{}'.format(database_name))

    def use_DataBases(self, databases_name='taoxu'):
        choice_databases = 'use ' + databases_name
        try:
            self.cursor.execute(choice_databases)
        except pymysql.err.Error as e:
            print(repr(e))
            databases_name = input('没有找到{}数据库，请重新输入：'.format(databases_name))
            self.use_DataBases(databases_name)
        else:
            print('连接数据库{}成功'.format(databases_name))
            return databases_name
            # 连接数据库成功后输出库里面的表名
            # self.show_BasesTable(databases_name)

    def del_DataBases(self, del_name):
        str_DelDataBases = 'drop database ' + del_name
        try:
            self.cursor.execute(str_DelDataBases)
            print('{}被删除'.format(del_name))
        except pymysql.err.Error as e:
            print(repr(e))
            del_name = input('您输入的数据库名有误或没有找到该数据库，请重新输入：')
            self.del_DataBases(del_name)

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

    def change_Table(self, change_type, change_range):
        pass

    def show_BasesTable(self, databases='taoxu'):
        str_ShowDataBases = 'show tables ' + databases
        self.cursor.execute(str_ShowDataBases)
        print('数据库{}的表为：'.format(databases))
        for BasesTable_name in self.cursor.fetchall():
            print(str(BasesTable_name).rstrip(')').lstrip('(').rstrip(','))
    # 创建数据库
    # Mysql_new.create_database(input('创建数据库:'))

    # 创建数据库表
    # Mysql_new.create_Datatable(input('请输入您想要创建的数据表名'), input(
    #     '输入您想要创建的数据表的字段名和字段类型（请以name varchar(25),age int这样为模板）'))  # 'name varchar(25),age int,ce int'

    #


if __name__ == '__main__':
    # 创建一个操作数据库的实例
    Mysql_new = Mysql_Operation()
    while True:
        try:
            button = int(input('请根据选项输入您所需要的功能\n'
                               '（1）查看数据库\n'
                               '（2）创建数据库\n'
                               '（3）选择控制的数据库\n'
                               '（4）删除数据库\n'
                               '（q）退出数据库控制系统'))
        except ValueError:
            print('您的输入有误，请根据已有功能选项重新输入')
            button = int(input('请根据选项输入您所需要的功能\n'
                               '（1）查看数据库\n'
                               '（2）创建数据库\n'
                               '（3）选择控制的数据库\n'
                               '（4）删除数据库\n'
                               '（5）查看表\n'
                               '（6）退出数据库管理系统\n'))
        else:
            if button == 1:
                Mysql_new.show_DataBases()
            elif button == 2:
                create_databasesname = input('请输入您需要创建的数据库名称（输入quit返回上一级）：')
                if create_databasesname == 'quit':
                    continue
                else:
                    Mysql_new.create_DataBases(create_databasesname)
            elif button == 3:
                Mysql_new.use_DataBases(input('请输入您想要控制的数据库名称'))
            elif button == 4:
                Mysql_new.del_DataBases(input('请输入您想要删除的数据库名称'))
            elif button == 5:
                Mysql_new.show_BasesTable()
            elif button == 6:
                print('退出数据库管理系统')
                break
