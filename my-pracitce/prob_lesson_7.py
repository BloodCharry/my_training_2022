# -*- coding: utf-8 -*-

# класс человек Man
from random import randint

from more_termcolor import cprint


class Man:
    # __инит__ (селф, нейм ) - это атрибуты
    def __init__(self, name):
        # имя человека name
        self.name = name
        # степень сытости fulness
        self.fulness = 50
        # # немного еды food
        # self.food = 50
        # # немного денег
        # self.money = 0
        # атрибут дом
        self.house = None
        # пишим методы что может делать человек
        # метод str чтобы вывести на консоль

    def __str__(self):
        return 'Я - {}, сытость  {}'.format(
            self.name, self.fulness)
        # человек может есть

    def eat(self):
        if self.house.food >= 10:
            cprint('{} Поел'.format(self.name), 'red')
            self.fulness += 10
            self.house.food -= 10
        else:
            print('{} нет еды'.format(self.name))

    # человек идёт на работу

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 50
        self.fulness -= 10

    # человек играет
    def watch_mtv(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fulness -= 10

    # поход в магазин
    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.food += 50
            self.house.money -= 50
        else:
            cprint('у {} нет денег'.format(self.name), color='red')

    # метод вьхеать в дом
    # house в какой дом мы вьезжаем
    # но программа может упасть поэтому атрибут прописываем в __инит__

    def go_into_the_house(self, house):
        self.house = house
        self.fulness -= 10
        cprint('{} вьехал в дом'.format(self.name), color='blue')

    # действие человека
    def act(self):
        if self.fulness <= 0:
            cprint('{} умер от голода'.format(self.name), color='red')
            return
        # кубик ( dice )
        dice = randint(1, 6)
        # cprint('выпало число {}'.format(dice), color='grey')
        if self.fulness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        # вася встаёт и кидает кубик (dice)
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_mtv()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0

    def __str__(self):
        return 'Еды в доме {}, денег в доме  {}'.format(
            self.food, self.money)


# сделаем много жителей
residents = [Man(name='Бивис'),
             Man(name='Батхет'),
             Man(name='Пиридурок')
             ]
# bivis = Man(name='Бивис')
# bathet = Man(name='Батхет')
# заселим людей в дом
my_sweet_house = House()
# сделаем цикл для дома
for resident in residents:
    resident.go_into_the_house(house=my_sweet_house)

# заставим людей жить
# цикл дней

for day in range(1, 366):
    cprint('============= день {} =============='.format(day), color="yellow")
    for resident in residents:
        resident.act()
    # люди действие
    # bivis.act()
    # bathet.act()
    print('---------------------------------------')
    for resident in residents:
        print(resident)
    cprint(my_sweet_house, color='blue')

