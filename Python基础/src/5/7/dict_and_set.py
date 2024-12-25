d = {
    'a': 1,
    'b': '2',
    'c': True
}

d['d'] = [1, 2, 3]

print(d['d'])
print('f' in d)
print(d.get('a'))
print(d.get('g', 6))
print(d.pop('d'))
print(d.get('d'))
d.update({'a': 1, 'b': '2'})
d.update(c=3, d=4)
d.update([('e', 5)])
print(d)

s = {1, 2, 3}
s2 = set([4, 5, 6])
s.add(4)
s.remove(1)
print(s & s2)
print(s | s2)
s.update([3, 4, 5, 6, 7, 8])
print(s.pop())
