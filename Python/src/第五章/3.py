n = 21
result = 0

for i in range(1, n):
    tmp = 1
    for j in range(1, i + 1):
        tmp *= j
    result += tmp

print(result)

for i in range(1, 10):
    print(i)
