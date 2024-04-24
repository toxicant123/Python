year = input('请输入年份：')

if not year.isdigit():
    print('请输入数字')
    exit(255)

year = int(year)

if not year % 400 or (not year % 4 and year % 100):
    print('是闰年')
else:
    print('不是闰年')
