# Python基础

# 1. 输入与输出

| 方法      | 示例                   |
|---------|----------------------|
| input() | a = input('请输入您的名字') |
| print() | print('Hello World') |

```python
# input函数的返回值为string
num_str = input('请输入一个数字：')

print('该数字的立方为', float(num_str) ** 3)
```

# 2. 基础

## 2.1 数据类型

| 类型  | 示例                                                                                                           |
|-----|--------------------------------------------------------------------------------------------------------------|
| 整数  | 100, 0xff00, 10_000_000                                                                                      |
| 浮点数 | 1.23, 3.5e9, 1.4e-6                                                                                          |
| 字符串 | 'a', "b", '"', "I'm ok", 'you\\'re ok?', 'a\nb\nc', r'a\nb\nc', '''a1<br/>b2<br/>c3''', r'''a1<br/>b2\nc3''' |
| 布尔值 | Ture, False                                                                                                  |
| 空值  | None                                                                                                         |
| 字节  | b'A', b'\xe4\xb8\xad\xe6\x96\x87'                                                                            |

```python
num1 = 100
num2 = 0xff00
num3 = 10_000_000

print(num1, num2, num3)

float1 = 1.23
float2 = 3.5e9
float3 = 1.4e-6

print(float1, float2, float3)

str1 = 'a'
str2 = "b"
str3 = '"'
str4 = "I'm ok"
str5 = 'you\'re ok?'
str6 = 'a\nb\nc'
str7 = r'a\nb\nc'
str8 = '''a1
b2
c3'''
str9 = r'''a1
b2\nc3'''

print(str1, str2, str3, str4, str5, str6, str7, str8, str9)

bool1 = True
bool2 = False

print(bool1, bool2)

none1 = None

print(none1)
```

| 运算符 | 示例            |
|-----|---------------|
| and | True and True |
| or  | True or False |
| not | not Ture      |

```python
bool1 = True and True
bool2 = True or False
bool3 = not True

print(bool1, bool2, bool3)
```

## 2.2 字符串和编码

| 方法          | 示例                   | 作用             |
|-------------|----------------------|----------------|
| ord()       | ord('A')             | 获取unicode编码    |
| chr()       | chr(66)              | 将unicode编码转为字符 |
| ''.encode() | 'A'.encode('utf-8')  | 将字符串编码为字节      |
| ''.decode() | b'A'.decode('utf-8') | 将字节解码为字符串      |

```python
print(ord('A'))
print(ord('中'))

print(chr(66))
print(chr(33421))

print('中文'.encode('utf-8'))
chinese = b'\xe4\xb8\xad\xe6\x96\x87'
print(chinese.decode('utf-8'))

print(len('中文'))
print(len(chinese))
```

### 2.2.1 格式化

| 占位符 | 替换内容    | 备注                            |
|-----|---------|-------------------------------|
| %d  | 	整数     | %nd表示将数字补空格至n位，%0nd表示将数字补0至n位 |
| %f  | 	浮点数    | $.nf表示保留n位小数的浮点数              |
| %s  | 	字符串    |                               |
| %x  | 	十六进制整数 |                               |

```python
print('Hi, Mr.%s, You have %d' % ('Tom', 10000))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('reduce %d%%' % 3)
```

| 方法       | 示例                  | 作用     |
|----------|---------------------|--------|
| format() | 'a {0}'.format('b') | 格式化字符串 |

f-string，即f开头的字符串也可以用于格式化

```python
str1 = 'Hello, {0}. Your score improved {1:.1f}%'.format('XiaoMing', 14)
print(str1)

r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')
```

## 2.3 list和tuple

| 方法    | 示例              | 作用              |
|-------|-----------------|-----------------|
| len() | [1, 2, 3].len() | 获取list或tuple的长度 |













