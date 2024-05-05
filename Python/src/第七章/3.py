pwd = input('请输入密码：')

if len(pwd) < 8:
    raise Exception('len < 8')
