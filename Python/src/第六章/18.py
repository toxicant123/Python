users_and_password = {
    '小红': {
        'password': '123',
        'status': True
    },
    'mia': {
        'password': '456',
        'status': True
    },
    'jack': {
        'password': '789',
        'status': False
    }
}

print(users_and_password)

for i in range(3):
    user = input('请输入你的用户名：')
    pwd = input('请输入你的密码：')
    if user in users_and_password.keys():
        data = users_and_password.get(user)
        if data['status']:
            if pwd == data['password']:
                print('登录成功')
                break
            else:
                print('账号或密码错误')
        else:
            print('账号失效，请联系管理员')
    else:
        print('该用户不存在，请先注册')