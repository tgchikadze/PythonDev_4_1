'''
Приложение для работы с файлами.
Функционал:
1. Рекурсивный обход директории, копирование с переименованием
всех найденных файлов с расширением TSV в заданный каталог:
tsv_parser(path: str = None)
2. Рекурсивный обход директории, копирование
всех найденных файлов с указанной датой последнего изменения в заданный каталог:
date_parser(path: str = None, date)
3. Diff - сравнение содержимого двух текстовых файлов
...
Данный файл проекта содержит функционал, необходимый для запуска консольного приложения
'''
#new_file_name: f'discovered_file_{i}.tsv')
'''
Импорты:
'''

import platform
import sys
import argparse
import pandas as pd
import numpy as np
import os


try:
    from custom_parser import my_parser, my_copier, my_renamer
except:
    print("Библиотека или функции не найдены")

'''
Парсер командной строки
'''

def command_parser(*args, **kwargs):
    '''
    Функция берет на вход командную строку и парсит ее содержимое.
    Затем запускает соответствующую функцию из custom_parser.py

    Командная строка должна включать вызов приложения, команду и параметры (путь или дату в зависимости от команды)

    :param args:
    :param kwargs:
    :return:
    '''
    parser = argparse.ArgumentParser("Command parser")  # заводим основной парсер
    subparsers = parser.add_subparsers(dest='command', required=True)  # заводим основной подпарсер

    parser_01 = subparsers.add_parser("my_parser", help="parses files by type or/and date")
    parser_01.add_argument("x", type=int, help='first number')
    parser_01.add_argument("y", type=int, help='second number')
    parser_01.set_defaults(func='my_parser')

    parser_sub = subparsers.add_parser("sub", help="subs two numbers")
    parser_sub.add_argument("x", type=int, help='first number')
    parser_sub.add_argument("y", type=int, help='second number')
    parser_sub.set_defaults(func='sub')

    argv = parser.parse_args()
    print(argv)
    commands = {'add': add, 'sub': sub}
    print(commands[argv.command](argv.x, argv.y))







command_parser()
print('Done')
