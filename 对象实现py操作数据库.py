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

            # 使用cursor()方法创建一个游标对象cursor
            self.cursor = self.conn.cursor()

        except pymysql.err.Error as e:  # as 和except组合使用，将捕获到的异常对象赋值给e
            print('连接数据库后台失败{}'.format(e))
        else:
            print('连接数据库后台成功')

    def show_DataBases(self):  # 查看所有数据库
        str_ShowDataBases = 'show databases'
        self.cursor.execute(str_ShowDataBases)
        print('数据库：')
        for databases_name in self.cursor:
            print(databases_name)

    def create_DataBases(self, database_name):  # 创建数据库
        create_base = 'create database ' + database_name
        try:
            self.cursor.execute(create_base)
        except pymysql.err.ProgrammingError as e:
            print(repr(e))
            # repr()函数将对象转化为供解释器读取的形式。
            # dict = {'runoob': 'runoob.com', 'google': 'google.com'};
            # repr(dict)
            # "{'google': 'google.com', 'runoob': 'runoob.com'}"
        else:
            print('创建数据库成功：{}'.format(database_name))

    def use_DataBases(self, databases_name='taoxu'):  # 选择控制数据库
        choice_databases = 'use ' + databases_name + ';'
        try:
            self.cursor.execute(choice_databases)
        except pymysql.err.Error as e:
            print(repr(e))
            databases_name = input('没有找到{}数据库，请重新输入：'.format(databases_name))
            self.use_DataBases(databases_name)
        else:
            print('连接数据库{}成功'.format(databases_name))
            # 连接数据库成功后输出库里面的表名
            self.show_BasesAllTable(databases_name)

    def del_DataBases(self, del_name):  # 删除数据库
        str_DelDataBases = 'drop database ' + del_name
        try:
            self.cursor.execute(str_DelDataBases)
            print('{}被删除'.format(del_name))
        except pymysql.err.Error as e:
            print(repr(e))
            del_name = input('您输入的数据库名有误或没有找到该数据库，请重新输入：')
            self.del_DataBases(del_name)

    def show_BasesAllTable(self, databases='taoxu'):  # 查看数据库的所有表
        str_ShowDataBases = 'select table_name from information_schema.`tables`a where a.TABLE_SCHEMA = \'' \
                            + databases + '\';'
        self.cursor.execute(str_ShowDataBases)
        print('数据库{}的表为：'.format(databases))
        for BasesTable_name in self.cursor.fetchall():
            print(str(BasesTable_name).rstrip(')').lstrip('(').rstrip(','))

    def show_BasesTable(self, table_name):  # 查询数据表的结构
        str_ShowDataBases = 'desc ' + table_name + ';'
        try:
            self.cursor.execute(str_ShowDataBases)
        except pymysql.err.Error as e:
            print('查看数据表失败')
            print(repr(e))
        else:
            print('{:<20}{:<19}{:<19}{:<20}{:<19}{:<16}'.format('字段', '类型', '可否为空', '主键', '默认值', '额外的信息'))
            for field_all in self.cursor.fetchall():
                for field_one in field_all:
                    print('{:<21}'.format(str(field_one)), end='')
                print('')

    def create_DataTable(self, table_name, *args):
        str_args = str(args)
        str_createtable = 'create table ' + table_name + \
                          ' (id int unsigned not null auto_increment PRIMARY KEY,' + str_args[2:-3] + ');'
        try:
            self.cursor.execute(str_createtable)
        except pymysql.err.Error as e:
            print('创建数据表失败')
            if repr(e) == 'OperationalError(1046, \'No database selected\')':
                print('没有选择数据库')
                self.use_DataBases(input('请选择您需要控制的数据库'))
            else:
                table_name = str(input('请重新输入您想要创建的数据表名：'))
                args = input('请重新输入您想要创建的数据表里的字段和字段类型：')
                self.create_DataTable(table_name, args)
        else:
            print(str_createtable)
            print('创建数据表{}成功'.format(table_name))

    def change_Table(self, change_type, change_tableName, change_range):  # 修改数据表

        # ALTER TABLE <表名> ADD <新字段名> <数据类型> [约束条件] [FIRST|AFTER 已存在的字段名]；
        if change_type == 'add':
            str_changetable = 'alter table ' + change_tableName + ' add ' + change_range
            try:
                self.cursor.execute(str_changetable)
            except pymysql.err.ProgrammingError as e:
                print(repr(e))
                print('添加失败，请检查您的输入是否正确')
            else:
                print('添加成功')
        elif change_type == 'change':
            str_changetable = 'alter table ' + change_tableName + ' modify ' + change_range
            try:
                self.cursor.execute(str_changetable)
            except pymysql.err.ProgrammingError as e:
                print(repr(e))
                print('修改失败，请检查您的输入是否正确')
            else:
                print('修改成功')
                self.show_BasesTable(change_tableName)


if __name__ == '__main__':
    # 创建一个操作数据库的实例
    Mysql_new = Mysql_Operation()
    while True:
        try:
            button = int(input('请根据选项输入您所需要的功能\n'
                               '（1）查看所有数据库\n'
                               '（2）创建数据库\n'
                               '（3）选择控制的数据库\n'
                               '（4）删除数据库\n'
                               '（5）查看数据库的所有表\n'
                               '（6）查看数据表的结构\n'
                               '（7）创建数据表\n'
                               '（8）修改数据表\n'
                               '（9）删除数据表\n'
                               '（max）退出数据库控制系统\n'))
        except ValueError:
            print('您的输入有误，请根据已有功能选项重新输入')
            button = int(input('请根据选项输入您所需要的功能\n'
                               '（1）查看所有数据库\n'
                               '（2）创建数据库\n'
                               '（3）选择控制的数据库\n'
                               '（4）删除数据库\n'
                               '（5）查看数据库的所有表\n'
                               '（6）查看数据表的结构\n'
                               '（7）创建数据表\n'
                               '（8）修改数据表\n'
                               '（9）删除数据表\n'
                               '（max）退出数据库管理系统\n'))
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
                use_databasesname = input('请输入您想要控制的数据库名称（输入quit返回上一级）：')
                if use_databasesname == 'quit':
                    continue
                else:
                    Mysql_new.use_DataBases(use_databasesname)

            elif button == 4:
                del_databasesname = input('请输入您想要删除的数据库名称（输入quit返回上一级）：')
                if del_databasesname == 'quit':
                    continue
                else:
                    Mysql_new.del_DataBases(del_databasesname)

            elif button == 5:
                show_basestablename = input('请输入您想要查询数据库（输入quit返回上一级）')
                if show_basestablename == 'quit':
                    continue
                else:
                    Mysql_new.show_BasesAllTable(show_basestablename)

            elif button == 6:
                show_tablename = input('请输入您想要查询的数据表名字（输入quit返回上一级）')
                if show_tablename == 'quit':
                    continue
                else:
                    Mysql_new.show_BasesTable(show_tablename)

            elif button == 7:
                create_tablename = str(input('请输入您需要创建的数据表名（输入quit返回上一级）'))
                if create_tablename == 'quit':
                    continue
                else:
                    # 创建的表里的字段名字和类型
                    create_tablefield = input('输入您想要创建的数据表的字段名和字段类型（请以name varchar(25),age int这样为模板）')
                    if create_tablefield == 'quit':
                        continue
                    else:
                        Mysql_new.create_DataTable(create_tablename, create_tablefield)

            elif button == 8:
                create_button = int(input('请选择您要对数据表的操作：\n'
                                          '（1）添加字段\n'
                                          '（2）修改字段数据类型\n'
                                          '（3）删除字段\n'
                                          '（4）修改字段名称\n'
                                          '（5）修改表名\n'
                                          '（6）返回\n'))
                if create_button == 1:
                    change_tablename = input('请输入您想要修改的表的名字')
                    add_fieldname = input('请输入您想要添加的字段名')
                    add_fieldtype = input('请输入您想要添加的字段的类型')
                    Mysql_new.change_Table('add', change_tablename, add_fieldname + ' ' + add_fieldtype)
                elif create_button == 2:
                    change_tablename = input('请输入您想要修改的表的名字')
                    change_field = input('请输入您想要修改的字段名')
                    change_fieldtype = input('请输入您想要修改的字段类型')
                    Mysql_new.change_Table('change', change_tablename, change_field + ' ' + change_fieldtype)
                elif create_button == 3:
                    del_tablename = input('请输入您想要修改的表的名字')
                    del_range = input('请输入您想要删除的字段名')
                    Mysql_new.change_Table('del', del_tablename, del_range)
                elif create_button == 4:
                    change_tablename = input('请输入您想要修改的表的名字')
                    change_oldfieldname = input('请输入您想要修改的字段名')
                    change_newfieldname = input('请输入修改后的字段名')
                    Mysql_new.change_Table('change', )
                elif create_button == 6:
                    continue
            elif button == 200:
                print('您已经退出数据库管理系统\n欢迎下次使用')
                break
            # 创建数据库
            # Mysql_new.create_database(input('创建数据库:'))

            # 创建数据库表
            # Mysql_new.create_Datatable(input('请输入您想要创建的数据表名'), input(
            #     '输入您想要创建的数据表的字段名和字段类型（请以name varchar(25),age int这样为模板）'))  # 'name varchar(25),age int,ce int'
            # 查询当前是否选择了控制数据库
            # self.cursor.execute('select database()')
            # print(str(self.cursor.fetchone()).rstrip(',)').lstrip('('))
            # if str(self.cursor.fetchone()).rstrip(',)').lstrip('(') == 'None':
            #     print('您好，请先选择操作的数据库再查询数据库里的表哦')
            #     self.use_DataBases(input('请输入您想要控制的数据库名：'))
