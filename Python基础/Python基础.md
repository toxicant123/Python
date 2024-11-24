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

























