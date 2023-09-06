# -*-coding: utf-8-*-
import csv
import json
import re
from collections import defaultdict
from datetime import datetime

from _decimal import Decimal, ROUND_HALF_EVEN

# Регулярное вырожение, только цифры: \d
re_data = r'jbd(\d{6})'
# регулярка только буквы : \w+
re_city = r'jbc(\w+)jbc'

re_expenses = r'jbe(\d+\.\d+)jbe'

with open('external_data/Bond.json', 'r') as data_file:
    data = json.load(data_file)

exchanges = {
    'токио': Decimal(0.7),  # японские йены -> фунт
    'москва': Decimal(0.12),  # рубль -> фунт
    'лондон': Decimal(1.0),  # фунт -> фунт
    'берлин': Decimal(0.87)  # евро -> фунт
}


# функция реформатирования
def str_to_datetime(date_str):
    return datetime.strptime(date_str, '%d%m%y')


# функция конверции валюты
def expencese_str_to_decimal(expenses_str, city):
    return Decimal(expenses_str) * exchanges[city]


# состовляем результирующий массив
result = []
for key, message in data.items():
    date_str = re.search(re_data, message)[1]
    city = re.search(re_city, message)[1]
    expenses_str = re.search(re_expenses, message)[1]
    result.append({
        'date': str_to_datetime(date_str),
        'city': city,
        'expenses': expencese_str_to_decimal(expenses_str, city)
    })

result = sorted(result, key=lambda record: record['date'])

# генерируем подробный файл
result_formated = [
    {"date": record['date'].strftime('%d.%m.%Y'),
     'city': record['city'],
     'expenses': str(record['expenses'].quantize(Decimal('1.00'), ROUND_HALF_EVEN))
     }
    for record in result
]

with open('external_data/BondDeatale.csv', 'w', encoding='utf-8', newline='') as out_detale_file:
    writer = csv.DictWriter(out_detale_file, fieldnames=['date', 'city', 'expenses'])
    writer.writeheader()
    writer.writerows(result_formated)

# агригируем по месяцам
result_aggregated_temp = defaultdict(lambda: {'cites': set(), 'expenses_sum': Decimal(0),
                                              'month': '', 'date_for_sort': None})
for record in result:
    month_datetime = datetime(year=record['date'].year, month=record['date'].month, day=1)
    month = month_datetime.strftime('%m.%Y')
    result_aggregated_temp[month]['cites'].add(record['city'])
    result_aggregated_temp[month]['expenses_sum'] += record['expenses']
    result_aggregated_temp[month]['month'] = month
    result_aggregated_temp[month]['date_for_sort'] = month_datetime

result_aggregated = sorted(result_aggregated_temp.values(), key=lambda record: record['date_for_sort'])

# генермруем в агригированный файл
result_aggregated_formated = [
    {
        "month": record['month'],
        'cites': ','.join(record['cites']),
        'expenses_sum': str(record['expenses_sum'].quantize(Decimal('1.00'), ROUND_HALF_EVEN))
    }
    for record in result_aggregated
]

with open('external_data/BondMounth_By.csv', 'w', encoding='utf-8', newline='') as out_mounth_file:
    writer = csv.DictWriter(out_mounth_file, fieldnames=['month', 'cites', 'expenses_sum'])
    writer.writeheader()
    writer.writerows(result_aggregated_formated)
