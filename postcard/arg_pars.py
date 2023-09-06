#                                   -*- coding: utf-8 -*-
import argparse
import os
from ticket_01 import MakeTicket

parser = argparse.ArgumentParser()
parser.add_argument('--fio', required=True, help='ФИО пассажира')
parser.add_argument('--from_city', required=True, help='Город отправления')
parser.add_argument('--to', required=True, help='Город прибытия')
parser.add_argument('--date', required=True, help='Дата вылета в формате дд.мм.гггг')
parser.add_argument('--template', default='images\\ticket_template.png', help='Путь к изображению шаблона')
parser.add_argument('--font', default=os.path.join("fonts", 'ofont.ru_Montserrat.ttf'), help='Путь к файлу шрифта')
parser.add_argument('--out_path', help='Путь к файлу выходного изображения')
args = parser.parse_args()

ticket = MakeTicket(fio=args.fio, from_city=args.from_city, to=args.to,
                    date=args.date, template=args.template, font_path=args.font)
ticket.fill(out_path=args.out_path)

# Вызвать скрипт:
# python arg_pars.py --fio "Иванов Иван Иванович"
# --from "Москва" --to "Санкт-Петербург" --date "2022-05-01" --out "ticket.png"