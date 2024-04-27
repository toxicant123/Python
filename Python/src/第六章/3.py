list1 = [1, 2, 3, 4, 5]

list2 = list1[0:2]

print(list2)

list2[0] = 3

print(list1, list2)

print(len(list1), len(list2))

for i, e in enumerate(list1):
    print(i, e)

del list1
