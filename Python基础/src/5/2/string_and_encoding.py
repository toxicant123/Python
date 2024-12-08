print(ord('A'))
print(ord('中'))

print(chr(66))
print(chr(33421))

print('中文'.encode('utf-8'))
chinese = b'\xe4\xb8\xad\xe6\x96\x87'
print(chinese.decode('utf-8'))

print(len('中文'))
print(len(chinese))
