from collections.abc import Iterable
from collections.abc import Iterator

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('', Iterator))
print(isinstance((x for x in range(10)), Iterator))
print(isinstance(100, Iterator))

print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
