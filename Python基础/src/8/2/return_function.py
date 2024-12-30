def lazy_sum(*args):
    def sub_sum():
        result = 0
        for arg in args:
            result += arg
        return result

    return sub_sum


result_f = lazy_sum(1, 2, 3, 4)
print(result_f())


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


def count2():
    def f(i):
        def g():
            return i * i

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f4, f5, f6 = count2()
print(f4(), f5(), f6())


def inc():
    x = 0

    def fn():
        nonlocal x
        x += 1
        return x

    return fn


f = inc()
print(f())
print(f())
print(f())
