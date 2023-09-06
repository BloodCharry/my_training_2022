# -*- coding: utf-8 -*-

class BowlingResult:
    def __init__(self, game_result):
        self.game_result = game_result
        self.prev_values = []
        self.score = 0
        self.frame = 0
        self.throw = 0
        self.result = self.game_result.split()
        self.val = None

    def check_result(self):
        if type(self.game_result) is not str:
            raise TypeError(f'Тип данных должен быть str, а у наc{type(self.game_result)}')
        len_res = len(self.result)
        if len_res < 12 or len_res > 21:
            raise ValueError("Неверное количество бросков")
        for i in self.result:
            if i.isalpha():
                if i == 'X' or i == '/':
                    continue
                if i.isdigit():
                    continue
                else:
                    raise ValueError(f'Недопустимые данные {i}')

    def get_score(self):
        self.check_result()
        for i in self.result:
            if self.frame == 10:
                self.frame_ten(i)
            else:
                self.check_throw(i)
        if self.frame != 10:
            raise ValueError(f'Количество фреймов должно быть ровно 10, а у вас: {self.frame}')
        return self.score

    def frame_ten(self, i):
        if self.throw == 0:
            self.check_ten_frame(i)
        elif self.throw == 1:
            self.check_ten_frame_bon(i)
        elif self.throw == 2:
            for idx in reversed(range(len(self.result))):
                if self.result[idx] == i:
                    self.val = idx
                    break
            if len(self.result) > self.val:
                raise ValueError(f'Фреймов должно быть ровно 10!')

    def check_throw(self, i):
        if self.throw == 1:
            self.throw_one(i)
        elif self.throw == 2:
            self.frame += 1
            self.throw = 0
        if i.isdigit():
            self.is_it_a_number(i)
        else:
            self.strike_sper(i)

    def throw_one(self, i):
        if i == '/':
            value = self.prev_values[-1]
            if value == 'X':
                raise ValueError('Некорректные данные')
            elif value == '/':
                raise ValueError('Некорректные данные')
            else:
                self.score = self.score - int(value) + 15
                self.throw += 1

    def is_it_a_number(self, i):
        if int(i) > 9:
            raise ValueError('Недопустимое количество очков, проверьте данные')
        else:
            self.score += int(i)
            self.throw += 1
            self.prev_values.append(i)

    def strike_sper(self, i):
        if i == '/' and self.throw == 0:
            raise ValueError('Неккоректные данные, sper не может быть первым броском')
        if i == 'X':
            self.score += 20
            self.frame += 1
            self.throw = 0
        elif i == '-':
            self.throw += 1
        self.prev_values.append(i)

    def check_ten_frame(self, i):
        if i == 'X':
            self.score += 20
            self.throw += 1
            self.prev_values.append(i)
        elif i == '/':
            raise ValueError('Некорректные данные')
        else:
            if i.isdigit():
                self.is_it_a_number(i)

    def check_ten_frame_bon(self, i):
        if i == 'X':
            self.throw += 1
            self.score += 20
            self.prev_values.append(i)
        elif i == '/':
            self.check_prev_val()
        else:
            if i.isdigit():
                self.is_it_a_number(i)

    def check_prev_val(self):
        value = self.prev_values[-1]
        if value == 'X':
            raise ValueError('Некорректные данные')
        elif value == '/':
            raise ValueError('Некорректные данные')


if __name__ == '__main__':
    score = 'X 7 / 9 0 X 0 8 8 / 0 6 X X X 8 9'
    result = BowlingResult(game_result=score)
    total_score = result.get_score()
    print(f'Количество очков: {total_score}')
