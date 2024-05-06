while True:
    try:
        op = input('请输入一个四则运算式：')
        if '+' in op:
            a = op.split('+')
            result = int(a[0]) + int(a[1])
            print(result)
        elif '-' in op:
            a = op.split('-')
            result = int(a[0]) - int(a[1])
            print(result)
        elif '*' in op:
            a = op.split('*')
            result = int(a[0]) * int(a[1])
            print(result)
        elif '/' in op:
            a = op.split('/')
            result = int(a[0]) / int(a[1])
            print(result)
        elif op == 'C':
            print('感谢您使用本计算器')
            break
        else:
            raise Exception("不合法的输入：%s" % op)
    except Exception as e:
        print(e)