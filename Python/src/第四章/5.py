py_score = input('请输入你的python课程成绩：')

if not py_score.isdigit():
    print('python课程的成绩必须为数字')
    exit(255)

c_score = input('请输入你的c课程成绩：')

if not c_score.isdigit():
    print('c课程的成绩必须为数字')
    exit(255)

py_score = int(py_score)
c_score = int(c_score)
if py_score >= 60 or c_score >= 60:
    print('及格啦')
else:
    print('未及格')
