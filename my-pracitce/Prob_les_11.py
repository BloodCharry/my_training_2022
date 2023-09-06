# -*- coding utf-8 -*-
# # декоратор
# def statter_factory(n):
#     def stutter(text):
#         return (text[:2] + '-') * n + text
#
#     return stutter
#
#
# animal = 'Зайка'
# statter_2 = statter_factory(n=2)
# print(statter_2(animal))
# stutter_3 = statter_factory(n=3)
# print(stutter_3(animal))
#
# statters = [statter_factory(n=n) for n in range(1, 4)]
# print(statters)
# # генератор
# result = [func(animal) for func in statters]
# print(result)
#
# animals = ['зайка', 'мишка', 'бегемотик']
# mesh = [func(animal) for animal in animals for func in statters]
# print(mesh)
ops = {'*': lambda x, y: x * y,
       '/': lambda x, y: x / y,
       '//': lambda x, y: x // y,
       '%': lambda x, y: x % y,
       '+': lambda x, y: x + y,
       '-': lambda x, y: x - y,
       }


def calc(line):
    operand_1, operation, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if operation in ops:
        func = ops[operation]
        value = func(operand_1, operand_2)
    else:
        raise ValueError(f"Unknown operation {operation}")
    return value


def get_lines(file_name):
    with open(file_name, 'r') as ff:
        for line in ff:
            if not line:
                continue
            line = line[:-1]
            yield line


total = 0
for line in get_lines(file_name='D:\\programirovanie\\material_snipets\\10\\python_snippets\\calc.txt'):
    try:
        total += calc(line)
    except ValueError as exc:
        if 'unpack' in exc.args[0]:
            print(f'нехватает операндов {exc} в строке {line}')
        else:
            print(f'не могу преооброзовать к целому {exc} в строке {line}')

print(f'total = {total}')
