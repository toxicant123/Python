print(sorted([36, 5, -12, 9, -21]))

print(sorted([36, 5, -12, 9, -21], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

list1 = [113, 7, 19, 22, 51, 38, 40]

def get_last_num(num):
    return abs(num) % 10

print(sorted(list1, key=get_last_num))
