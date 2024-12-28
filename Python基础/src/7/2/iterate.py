from collections.abc import Iterable

list1 = [1, 2, 3]

for item in list1:
    print(item)

tuple1 = (1, 2, 3)

for item in tuple1:
    print(item)

dict1 = {
    'a': 1,
    'b': '2',
    'c': True
}

for k, v in dict1.items():
    print(k, v)

str1 = 'ABCDEFG'

for item in str1:
    print(item)

for i, e in enumerate(list1):
    print(i, e)

print('is iterable:', isinstance('abc', Iterable))
print('is iterable:', isinstance([1, 2, 3], Iterable))
print('is iterable:', isinstance(False, Iterable))
