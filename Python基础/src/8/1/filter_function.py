def is_odd(n):
    return n % 2 == 1


result_list = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(result_list)


def get_prime_number_list():
    n = 3
    while True:
        yield n
        n += 2


def exclude_not_prime_number(n):
    return lambda x: x % n > 0


def get_prime():
    yield 2
    item_iterator = get_prime_number_list()
    while True:
        n = next(item_iterator)
        yield n
        item_iterator = filter(exclude_not_prime_number(n), item_iterator)


for n in get_prime():
    if n < 100:
        print(n)
    else:
        break
