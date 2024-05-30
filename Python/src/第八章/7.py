a = int('165')

print(a)


def infos(name, age=24, gender='女'):
    return '大家好，我叫%s，我今年%d岁，我是一名%s生' % (name, age, gender)


print(infos('abb'))
print(infos('lily', 27))
print(infos('Tom', 19, '男'))
print(infos('Jack', gender='男'))


