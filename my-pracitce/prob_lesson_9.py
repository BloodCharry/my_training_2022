# -*-coding utf8 -*-
import zipfile

# zip_fil e_name = 'voyna-i-mir.txt.zip'
# # чтение зип файла
# zFile = zipfile.ZipFile(zip_file_name, 'r')
# # распоковка зип файлка
# for filename in zFile.namelist():
#     zFile.extract(filename)
from pprint import pprint
# делаем статистику
from random import randint


class Chatterer:
    analize_count = 4

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}

    # расзиповали
    def unzip(self):
        # чтение зип файла
        zFile = zipfile.ZipFile(self.file_name, 'r')
        # распоковка зип файлка
        for filename in zFile.namelist():
            zFile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        self.seqaense = ' ' * self.analize_count
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                # для форматирования делаем возврат каретки
                self.collect_for_line(line=line[:-1])

    def collect_for_line(self, line, seqaense):
        for char in line:
            # если предедущий есть в статистике
            if self.seqaense in self.stat:
                if char in self.stat[self.seqaense]:
                    self.stat[self.seqaense][char] += 1
                else:
                    self.stat[self.seqaense][char] = 1
            # если предедущего символа в статистике нету
            else:
                # организовываем словарик в котором будет статистика для одного символа
                self.stat[self.seqaense] = {char: 1}
            # следующий символ
            # без первого символа
            self.seqaense = self.seqaense[1:] + char

    def prepare(self):
        self.totals = {}
        # cловарь подготовленный для генерации
        self.stat_for_generate = {}
        for seqaense, char_stat in self.stat.items():
            self.totals[seqaense] = 0
            self.stat_for_generate[seqaense] = []
            # проходимся по второму словарю
            for char, count in char_stat.items():
                self.totals[seqaense] += count
                self.stat_for_generate[seqaense].append([count, char])
            self.stat_for_generate[seqaense].sort(reverse=True)

    def chat(self, N, out_file_name=None):
        N = 1000
        printed = 0
        if out_file_name is not None:
            file = open(out_file_name, 'w', encoding='utf-8')
        else:
            file = None
        seqaense = ' ' * self.analize_count
        spaces_printed = 0
        while printed < N:
            char = self._get_char(char_stat=self.stat_for_generate[seqaense], total=self.totals[seqaense])
            if file:
                file.write(char)
            else:
                print(char, end='')
            if char == ' ':
                spaces_printed += 1
                if spaces_printed >= 10:
                    if file:
                        file.write('\n')
                    else:
                        print()
                    spaces_printed = 0
            printed += 1
            seqaense = seqaense[1:] + char
        if file:
            file.close()

    def _get_char(self, char_stat, total):
        dice = randint(1, total)
        # считаем на какой позиции находится
        pos = 0
        for count, char in char_stat:
            pos += count
            if dice <= pos:
                break
        return char


chatterer = Chatterer(file_name='voyna-i-mir.txt')
chatterer.collect()
chatterer.prepare()
chatterer.chat(N=10000, out_file_name='out.txt')
# file_name = 'voyna-i-mir.txt'
#
# stat = {}
# analize_count = 4
# seqaense = ' ' * analize_count
# with open(file_name, 'r', encoding='cp1251') as file:
#     for line in file:
#         # print(line)
#         # для форматирования делаем возврат каретки
#         line = line[:-1]
#         for char in line:
#             # если предедущий есть в статистике
#             if seqaense in stat:
#                 if char in stat[seqaense]:
#                     stat[seqaense][char] += 1
#                 else:
#                     stat[seqaense][char] = 1
#             # если предедущего символа в статистике нету
#             else:
#                 # организовываем словарик в котором будет статистика для одного символа
#                 stat[seqaense] = {char: 1}
#             # следующий символ
#             # без первого символа
#             seqaense = seqaense[1:] + char
# pprint(stat)
# print(len(stat))
# подготавливаем статистику к генерации
# totals = {}
# # cловарь подготовленный для генерации
# stat_for_generate = {}
# for seqaense, char_stat in stat.items():
#     totals[seqaense] = 0
#     stat_for_generate[seqaense] = []
#     # проходимся по второму словарю
#     for char, count in char_stat.items():
#         totals[seqaense] += count
#         stat_for_generate[seqaense].append([count, char])
#     stat_for_generate[seqaense].sort(reverse=True)
# pprint(totals)
# pprint(stat_for_generate)
# теперь будем генерировать

# N = 1000
# printed = 0
# seqaense = ' ' * analize_count
# spaces_printed = 0
# while printed < N:
#     char_stat = stat_for_generate[seqaense]
#     total = totals[seqaense]
#     dice = randint(1, total)
#     # считаем на какой позиции находится
#     pos = 0
#     for count, char in char_stat:
#         pos += count
#         if dice <= pos:
#             break
#     print(char, end='')
#     if char == ' ':
#         spaces_printed += 1
#         if spaces_printed >= 10:
#             print()
#             spaces_printed = 0
#     printed += 1
#     seqaense = seqaense[1:] + char
