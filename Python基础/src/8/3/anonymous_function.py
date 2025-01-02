list1 = [1, 2, 3, 4, 5, 6, 7, 8]

print(list(map(lambda x: x * x, list1)))

f = lambda x: x * x


def build(x, y):
    return lambda: x * x + y * y
