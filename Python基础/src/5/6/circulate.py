names = ['Tom', 'Jerry', 'Jack']

for name in names:
    print(name)

for i, name in enumerate(names):
    print(i, name)

number_sum = 0
for x in range(100):
    number_sum += x

letter_str = ''
count = 26
while count > 0:
    letter_str += chr(97 + (26 - count))
    count -= 1

print(letter_str)
