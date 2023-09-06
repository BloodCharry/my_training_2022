# Возвращает список цифр  из числа
from random import randint


# получить цифры
def getDigits(num):
    return [int(i) for i in str(num)]


# Возвращает значение True, если в числе
# нет повторяющихся цифр
# в противном случае False
def noDuplicates(num):
    num_li = getDigits(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False


# Генерирует 4-значное число
# без повторяющихся цифр
def generateNum():
    while True:
        num = randint(1000, 9999)
        if noDuplicates(num):
            return num


# Возвращает общие цифры с точным
# совпадения (быки) и общие
# цифры в неправильном положении (коровы)
def numOfBullsCows(num, guess):
    bull_cow = [0, 0]
    num_li = getDigits(num)
    guess_li = getDigits(guess)
    for i, j in zip(num_li, guess_li):
        # присутствует общая цифра
        if j in num_li:
            # точное совпадение общих цифр
            if j == i:
                bull_cow[0] += 1
            # обычная цифра совпадает, но в неправильном положении
            else:
                bull_cow[1] += 1
    return bull_cow
