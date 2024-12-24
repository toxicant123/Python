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
