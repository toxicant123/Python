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

dict:

| 方法            | 示例                                                                           | 作用            |
|---------------|------------------------------------------------------------------------------|---------------|
| dict.get()    | d.get('a')                                                                   | 获取key为a的值     |
| dict.pop()    | d.pop('a')                                                                   | 获取并删除key为a的值  |
| dict.update() | d.update({'a': 1, 'b': '2'})<br/>d.update(c=3, d=4)<br/>d.update([('e', 5)]) | 更新dict的k、v键值对 |

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

set:

| 方法           | 示例                  | 作用            |
|--------------|---------------------|---------------|
| set.add()    | s.add(4)            | 向set内添加一个元素   |
| set.remove() | s.remove(4)         | 从set内移除一个元素   |
| set.update() | s.update([1, 2, 3]) | 向set内更新一组数据   |
| set.pop()    | s.pop()             | 随机弹出set内的一个元素 |

```python
s = {1, 2, 3}
s2 = set([4, 5, 6])
s.add(4)
s.remove(1)
print(s & s2)
print(s | s2)
s.update([3, 4, 5, 6, 7, 8])
print(s.pop())
```

# 3. 函数

## 3.1 调用函数

```python
print(abs(100))
print(abs(-50))

print(max(-1 , 1, 2, 3, 4))

print(int('32'))
print(float('4.42'))
print(str(True))
print(bool(1))
print(bool(''))

a = abs
print(a(-1))
```

## 3.2 定义函数

```python
import math

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-2))
# print(my_abs('3'))

def get_circle_area_and_perimeter(radius):
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return area, perimeter

circle_info = get_circle_area_and_perimeter(100)
print(circle_info)
```

pass:

作为占位符，防止语法报错

```python
def nop():
    pass

age = 19
if age >= 18:
    pass
```

## 3.3 函数的参数

位置参数：

```python
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(2, 2))
```

默认参数：

默认参数必须指向不变对象！

```python
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(2, n=3))
```

可变参数：

```python
def calc(*numbers):
    number_sum = 0
    for n in numbers:
        number_sum += n * n
    return number_sum

print(calc(1, 3, 5, 7))
num_arr = [9, 11, 137, 445]
print(calc(*num_arr))
```

关键字参数：

```python
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Adam', 45, gender='M', job='Engineer')
person_info = {'address': 'Ningbo'}
person('Tom', 2, **person_info)
```

命名关键字参数：

```python
def person2(name, age, *, city, job):
    print('name:', name, 'age:', age, 'other:', city, 'job:', job)

person2('Michael', 30, city='Ningbo', job='Engineer')

def person3(name, age, *args, city, job):
    print('name:', name, 'age:', age, 'args:', args, 'city:', city, 'job:', job)

person3('Michael', 30, 1, 2, city='Ningbo', job='Engineer')
```

在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

```python
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)
```

## 3.4 递归函数

```python
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(5))
print(fact(100))
```

# 4. 高级特性

## 4.1 切片

`a_list[a:b:c]`表示从索引a开始到索引b（不包括索引b）每c个取一个。a默认为0，b默认为`len(a_list)`，c默认为1

切片可以对list、tuple、str使用

```python
num_list = [1, 2, 3, 4, 5, 6, 7, 8]

print(num_list[0:3])
print(num_list[:3])
print(num_list[-2:-1])
print(num_list[-10:])
print(num_list[:])
print(num_list[::2])

num_tuple = (1, 2, 3, 4, 5)
print(num_tuple[1:4:2])

example_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(example_str[1::3])
```

## 4.2 迭代

```python
from collections.abc import Iterable

list1 = [1, 2, 3]

for item in list1:
    print(item)

tuple1 = (1, 2, 3)

for item in tuple1:
    print(item)

dict1 = {
    'a': 1,
    'b': '2',
    'c': True
}

for k, v in dict1.items():
    print(k, v)

str1 = 'ABCDEFG'

for item in str1:
    print(item)

for i, e in enumerate(list1):
    print(i, e)

print('is iterable:', isinstance('abc', Iterable))
print('is iterable:', isinstance([1, 2, 3], Iterable))
print('is iterable:', isinstance(False, Iterable))
```

## 4.3 列表生成式

在列表生成式中，`for`前是表达式，`for`后的`if`是过滤条件

```python
list1 = [x * x for x in range(10) if x % 2 == 0]
print(list1)

list2 = [m + n for m in 'ABC' for n in 'XYZ']
print(list2)

d = {
    'x': 'A',
    'y': 'B',
    'z': 'C'
}
list3 = [k + '=' + v for k, v in d.items()]
print(list3)

list4 = ['Hello', 'World', 'IBM', 'Apple']
list5 = [s.lower() for s in list4]
print(list5)

list6 = range(100)
list7 = [x if x % 2 == 0 else -x for x in list6]
print(list7)
```

## 4.4 生成器

生成器函数，在每次调用`next()`的时候执行，遇到`yield`语句返回，再次执行时从上次返回的`yield`语句处继续执行。

调用生成器函数会创建一个生成器对象，多次调用生成器函数会创建多个相互独立的生成器。

```python
g = (x * x for x in range(10))

for e in g:
    print(e)

def fib(max_num):
    n, a, b = 0, 0, 1
    while n < max_num:
        yield b
        a, b = b, a + b
        n += 1

for e in fib(100):
    print(e)
```

## 4.5 迭代器

可直接作用于for循环的对象统称为可迭代对象：`Iterable`

可以被next()函数调用并不断返回下一个值的对象称为迭代器：`Iterator`

想要把`Iterable`变成`Iterator`可以使用iter()函数

```python
from collections.abc import Iterable
from collections.abc import Iterator

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('', Iterator))
print(isinstance((x for x in range(10)), Iterator))
print(isinstance(100, Iterator))

print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
```

# 5. 函数式编程

## 5.1 高阶函数

```python
f = abs

print(f(-10))

def add(x, y, f):
    return f(x) + f(y)

print(add(-1, 2, abs))
```

## 5.2 返回函数

使用闭包时，对外层变量赋值前，需要先使用`nonlocal`声明该变量不是当前函数的局部变量。

```python
def lazy_sum(*args):
    def sub_sum():
        result = 0
        for arg in args:
            result += arg
        return result

    return sub_sum


result_f = lazy_sum(1, 2, 3, 4)
print(result_f())


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


def count2():
    def f(i):
        def g():
            return i * i

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f4, f5, f6 = count2()
print(f4(), f5(), f6())


def inc():
    x = 0

    def fn():
        nonlocal x
        x += 1
        return x

    return fn


f = inc()
print(f())
print(f())
print(f())
```
