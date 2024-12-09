list1 = [1, 2, 3]

print(list1)
print(list1[0])

list1.append(4)
print(list1)

list2 = [1, 2]
list2.insert(1, 3)
print(list2)

a = list1.pop()
b = list1.pop(0)
print(a, b)
print(list1)
