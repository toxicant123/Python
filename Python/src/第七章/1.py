import traceback

try:
    i = 1 / 0
    print(i)
except ZeroDivisionError as e:
    traceback.print_exc()
    print(e)
