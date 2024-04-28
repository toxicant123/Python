for i in range(100, 1000):
    str_i = str(i)
    total = 0
    for j in list(str_i):
        j_num = int(j)
        total += j_num * j_num * j_num
    if i == total:
        print(i)