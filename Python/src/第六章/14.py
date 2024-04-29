d = {
    'name': 'hxf',
    'age': 30,
    'gender': False,
    'money': 0
}

for k, v in d.items():
    print(k, v)

print(d.pop('name'))
print(d)

print(len(d))
