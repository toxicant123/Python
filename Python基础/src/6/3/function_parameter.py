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


