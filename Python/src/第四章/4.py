age = input('请输入年龄：')

if age.isdigit():
    age = int(age)
    if 0 <= age <= 120:
        print('合法的年龄')
    else:
        print('不合法的年龄')
else:
    print('请输入数字')

