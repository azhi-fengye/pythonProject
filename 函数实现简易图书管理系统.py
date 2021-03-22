books = []


def add():
    info = {}
    books_num = int(input('请输入ISBN号：'))
    books_name = input('请输入书名：')
    books_type = input('请输入类别：')
    books_price = float(input('请输入价格：'))
    info['ISBN号'] = books_num
    info['书名'] = books_name
    info['类别'] = books_type
    info['价格'] = books_price
    books.append(info)
    print('成功录入{}\n'.format(books_num))
    count = int(input('如果想继续录入则输入【1】:'))
    if count == 1:
        add()


def check():
    ISBN = int(input('请输入ISBN号进行查询'))
    for i in books:
        if i.get('ISBN号') == ISBN:
            print('ISBN号        书名        类别        价格')
            print('{}            {}           {}            {}'.format(i['ISBN号'], i['书名'], i['类别'], i['价格']))
        else:
            print('没有当前书籍')


def change():
    ISBN = int(input('请输入ISBN号：'))
    for i in books:
        if i.get('ISBN号') == ISBN:
            change_num = int(input('输入修改后的ISBN号：'))
            change_name = input('输入修改后的书名：')
            change_type = input('输入修改后的类别：')
            change_price = float(input('输入修改后的价格：'))
            i['ISBN号'] = change_num
            i['书名'] = change_name
            i['类别'] = change_type
            i['价格'] = change_price
            print('ISBN号        书名        类别        价格')
            print('{}            {}           {}            {}'.format(i['ISBN号'], i['书名'], i['类别'], i['价格']))


def delete():
    ISBN = int(input('请输入ISBN号：'))
    for i in books:
        if i.get('ISBN号') == ISBN:
            books.remove(i)
            print('提示：没有找到该图书')


while True:
    print('*********************************************************')
    print('欢迎使用【图书查询系统】')
    print()
    print('1.图书信息录入')
    print('2.图书查询')
    print('3.图书信息删除')
    print('4.图书信息修改\n')
    print('0.退出系统')
    print('*********************************************************')
    button = int(input('请输入数字进行功能选择：'))
    print('您的操作是{}'.format(button))
    if button == 1:
        add()
    elif button == 2:
        check()
    elif button == 3:
        delete()
    elif button == 4:
        change()
    elif button == 0:
        print('欢迎再次使用【图书查询系统】')
        break
    else:
        button = input('您的输入有误请重新输入')
