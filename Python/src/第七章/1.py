try:
    i = 1 / 0
    print(i)
except ZeroDivisionError as e:
    print(e)
