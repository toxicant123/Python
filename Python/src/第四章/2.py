score = input('请输入你的成绩：')

score = int(score)

if score > 100:
    print('TOO MUCH SCORE')
elif score >= 90:
    print('LEVEL A')
elif score >= 80:
    print('LEVEL B')
elif score >= 70:
    print('LEVEL C')
elif score >= 60:
    print('LEVEL D')
else:
    print('NO LEVEL')


