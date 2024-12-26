def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5))


def calc(*numbers):
    number_sum = 0
    for n in numbers:
        number_sum += n * n
    return number_sum


print(calc(1, 3, 5, 7))
num_arr = [9, 11, 137, 445]
print(calc(*num_arr))

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Adam', 45, gender='M', job='Engineer')
person_info = {'address': 'Ningbo'}
person('Tom', 2, **person_info)

def person2(name, age, *, city, job):
    print('name:', name, 'age:', age, 'other:', city, 'job:', job)

person2('Michael', 30, city='Ningbo', job='Engineer')

def person3(name, age, *args, city, job):
    print('name:', name, 'age:', age, 'args:', args, 'city:', city, 'job:', job)

person3('Michael', 30, 1, 2, city='Ningbo', job='Engineer')

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)
