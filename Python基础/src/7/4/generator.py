g = (x * x for x in range(10))

for e in g:
    print(e)

def fib(max_num):
    n, a, b = 0, 0, 1
    while n < max_num:
        yield b
        a, b = b, a + b
        n += 1

for e in fib(100):
    print(e)
