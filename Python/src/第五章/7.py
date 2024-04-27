for i in range(9):
    for j in range(i):
        left = i + 1
        right = j + 1
        result = left * right
        print('%d x %d = %d ' % (left, right, result), end='')
    print()