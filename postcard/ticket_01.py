#                               -*- coding: utf-8 -*-
import re
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor


class MakeTicket:

    def __init__(self, fio, from_city, to, date, template=None, font_path=None):
        self.fio = fio
        self.from_ = from_city
        self.to = to
        self.date = date
        self.template = 'images\\ticket_template.png' if template is None else template
        if font_path is None:
            self.font_path = os.path.join("fonts", 'ofont.ru_Montserrat.ttf')
        else:
            self.font_path = font_path

    def fill(self, out_path=None):
        im = Image.open(self.template)
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(self.font_path, size=16)
        self.f_i_o(im, font, draw)
        self._from_(im, font, draw)
        self._to_(im, font, draw)
        self.date_(im, font, draw)
        im.show()
        out_path = out_path if out_path else 'avia_prob.png'
        im.save(out_path)
        print(f'Post card saved az {out_path}')

    def f_i_o(self, im, font, draw):
        y = 124
        x = 47
        message = self.fio
        draw.text((x, y), message, font=font, fill=ImageColor.colormap['black'])

    def _from_(self, im, font, draw):
        y = 192
        x = 47
        message = self.from_
        draw.text((x, y), message, font=font, fill=ImageColor.colormap['black'])

    def _to_(self, im, font, draw):
        y = 258
        x = 47
        message = self.to
        draw.text((x, y), message, font=font, fill=ImageColor.colormap['black'])

    def date_(self, im, font, draw):
        y = 258
        x = 290
        message = self.date
        draw.text((x, y), message, font=font, fill=ImageColor.colormap['black'])


class CheckInt:

    def __init__(self):
        self.name = ''
        self.from_ = ''
        self.to = ''
        self.date = ''

    def check_fio(self):
        while True:
            self.name = input('Введите ваше имя, фамилию и отчество: ')
            parts = self.name.split()
            if len(parts) != 3:
                print('поле должно содержать фамилию имя отчество, попробуйте еще раз.')
                continue
            elif not all(re.match('^[а-яА-ЯёЁ]+$', part) for part in parts):
                print('Вы ввели некорректные данные, используйте только русские буквы.')
                continue
            else:
                break
        return self.name

    def check_from(self):
        while True:
            self.from_ = input('Введите точку отправления: ')
            parts = self.from_.split()
            if len(parts) != 1:
                print('поле должно содержать только город откуда вы отправляетесь, попробуйте еще раз.')
                continue
            elif not all(re.match('^[а-яА-ЯёЁ]+$', part) for part in parts):
                print('Вы ввели некорректные данные, используйте только русские буквы.')
                continue
            else:
                break
        return self.from_

    def check_to(self):
        while True:
            self.to = input('Введите точку прибытия: ')
            parts = self.to.split()
            if len(parts) != 1:
                print('поле должно содержать только город куда вы прибываете, попробуйте еще раз.')
                continue
            elif not all(re.match('^[а-яА-ЯёЁ]+$', part) for part in parts):
                print('Вы ввели некорректные данные, используйте только русские буквы.')
                continue
            else:
                break
        return self.to

    def check_data(self):
        while True:
            self.date = input('Введите дату в формате дд.мм.гггг: ')
            self.date = re.sub('[^0-9\.]+', '', self.date)
            if not re.match('^[0-9\.]+$', self.date):
                print('Вы ввели некорректные данные, попробуйте еще раз.')
                continue
            elif len(self.date) != 10 or self.date[2] != '.' or self.date[5] != '.':
                print('Дата должна быть в формате дд.мм.гггг, попробуйте еще раз.')
                continue
            else:
                day = int(self.date[:2])
                month = int(self.date[3:5])
                year = int(self.date[6:])
                if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 9999):
                    print('Вы ввели некорректную дату, попробуйте еще раз.')
                    continue
                else:
                    break
        self.date = '.'.join([str(day), str(month), str(year)])
        return self.date


if __name__ == '__main__':
    checking = CheckInt()
    name = checking.check_fio()
    from_ = checking.check_from()
    to = checking.check_to()
    date = checking.check_data()
    maker = MakeTicket(fio=name, from_city=from_, to=to, date=date)
    maker.fill()

