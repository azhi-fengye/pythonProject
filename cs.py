# # a = 12345678909876543
# # a = str(a)
# # print(len(a))
# # for i in a:
# #     print(i)
# # print(a[::-1])
# # b = list()
# # b.append(a)
# # print(b)
# import pymysql
#
# connection = pymysql.connect(
#
#     host='localhost',  # IP，MySQL数据库服务器IP地址
#     port=3306,  # 端口，默认3306，可以不输入
#     user='root',  # 数据库用户名
#     password='root',  # 数据库登录密码
#     database='taoxu',  # 要连接的数据库
#     charset='utf8'  # 字符集，注意不是utf-8
#
# )
# cr = connection.cursor()
# cr.execute('alter table hah modify age it;')
# for i in cr.fetchall():
#     for j in i:
#         print(j,end=' ')
#         print(type(j),end=' ')
#     print()
change_field = input('请输入您想要修改的字段名')
change_fieldtype = input('请输入您想要修改的字段类型')
print(change_fieldtype + change_field)
print(type(change_field))
print(type(change_fieldtype))
print(type(change_field + ' ' + change_fieldtype))
