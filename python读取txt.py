f = open('name.txt', 'r', encoding='utf8')
cs = f.read().split(',')
print(type(cs))
for i in cs:
    print(i)
f.close()
