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

def nop():
    pass

def get_circle_area_and_perimeter(radius):
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return area, perimeter

circle_info = get_circle_area_and_perimeter(100)
print(circle_info)
