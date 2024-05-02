s = set()

print(s, type(s))

s = {1, 2, 3, 4}

print(s)

s = set([1, 2, 3, 4, 5, 1, 2, 3, 4])

print(s)

s = set('123')

print(s)

s = set({1: 'a', 'a': 2})

print(s)

s.remove('a')

s.update('hello')

print(s)

s.add(2)

print(s)

s2 = {1, 2, 3, 4, 5}

print(s & s2)

print(s | s2)


