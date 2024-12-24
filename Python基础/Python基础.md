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

| 方法       | 示例                  | 作用                        |
|----------|---------------------|---------------------------|
| len()    | [1, 2, 3].len()     | 获取list或tuple的长度           |
| append() | [].append(1)        | 往list中添加元素到末尾             |
| insert() | [1, 2].insert(1, 3) | 往list的某个索引位置添加元素          |
| pop()    | pop(), pop(1)       | 删除指定位置的元素，若不传入索引则删除最后一个元素 |

```python
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
```

```python
t1 = ()
t2 = (1,)
t3 = (1, 2, 3)

print(t1, t2, t3, len(t3))
```

## 2.4 条件判断

if:

```python
score = 61
if score >= 80:
    print('优秀')
elif score >= 70:
    print('良好')
elif score >= 60:
    print('及格')
else:
    print('不及格')

x = 1
if x:
    print('x is Ture')
```

## 2.5 模式匹配

基础匹配：

```python
score = 'B'

match score:
    case 'A':
        print('score is A')
    case 'B':
        print('score is B')
    case 'C':
        print('score is C')
    case 'D':
        print('score is D')
    case _:
        print('score is unknown')
```

`_`表示匹配任意值

复杂匹配：

```python
age = 15

match age:
    case x if x < 10:
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')
```

匹配列表：

```python
args = ['gcc', 'hello.c', 'world.c']

match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')
```

## 2.6 循环

| 方法          | 示例                   | 作用               |
|-------------|----------------------|------------------|
| range()     | range(100)           | 生成一个从0-99的可迭代对象  |
| enumerate() | enumerate([1, 2, 3]) | 生成一个带有索引和值的可迭代对象 |

for:

```python
names = ['Tom', 'Jerry', 'Jack']

for name in names:
    print(name)

for i, name in enumerate(names):
    print(i, name)

number_sum = 0
for x in range(100):
    number_sum += x
```

while:

```python
letter_str = ''
count = 26
while count > 0:
    letter_str += chr(97 + (26 - count))
    count -= 1

print(letter_str)
```

break:

```python
for i in range(3):
    if i == 1:
        break
    print(i)
```

continue:

```python
for i in range(3):
    if i == 1:
        continue
    print(i)
```

## 2.7 dict和set

| 方法            | 示例                                                                           | 作用            |
|---------------|------------------------------------------------------------------------------|---------------|
| dict.get()    | d.get('a')                                                                   | 获取key为a的值     |
| dict.pop()    | d.pop('a')                                                                   | 获取并删除key为a的值  |
| dict.update() | d.update({'a': 1, 'b': '2'})<br/>d.update(c=3, d=4)<br/>d.update([('e', 5)]) | 更新dict的k、v键值对 |

dict:

```python
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
```

