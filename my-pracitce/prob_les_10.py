# -*- coding: utf-8 -*-
def calc(line):
    print(f'read line: {line}', flush=True)
    operand_1, operation, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if operation == '+':
        value = operand_1 + operand_2
    elif operation == '-':
        value = operand_1 - operand_2
    elif operation == '*':
        value = operand_1 * operand_2
    elif operation == '/':
        value = operand_1 / operand_2
    elif operation == '//':
        value = operand_1 // operand_2
    elif operation == '%':
        value = operand_1 % operand_2
    else:
        print(f'Unknown operation {operation}')
    return value


total = 0
with open('D:\\programirovanie\\material_snipets\\10\\python_snippets\\calc.txt', 'r') as ff:
    for line in ff:
        line = line[:-1]
        try:
            total += calc(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'нехватает операндов {exc} в строке {line}')
            else:
                print(f'не могу преооброзовать к целому {exc} в строке {line}')

print(f'total = {total}')
