def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(5))
print(fact(100))


def move(n: int, a: str, b: str, c: str) -> None:
    if n == 1:
        print(a, '-->', c)
        return
    move(n - 1, a, c, b)
    move(1, a, b, c)
    move(n - 1, b, a, c)

move(3, 'A', 'B', 'C')
