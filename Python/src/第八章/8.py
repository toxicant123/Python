def total(*a):
    result = 0
    for i in a:
        result += i
    return result


print(total(1, 2, 3, 4, 5))

print(total(*[100, 200, 300]))


def f(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


f(**{
    'a': 1, 'b': 2, 'c': 3
})

