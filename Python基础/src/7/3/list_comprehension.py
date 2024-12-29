list1 = [x * x for x in range(10) if x % 2 == 0]
print(list1)

list2 = [m + n for m in 'ABC' for n in 'XYZ']
print(list2)

d = {
    'x': 'A',
    'y': 'B',
    'z': 'C'
}
list3 = [k + '=' + v for k, v in d.items()]
print(list3)

list4 = ['Hello', 'World', 'IBM', 'Apple']
list5 = [s.lower() for s in list4]
print(list5)

list6 = range(100)
list7 = [x if x % 2 == 0 else -x for x in list6]
print(list7)
