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
    import custom_parser
except:
    print("Библиотека не найдена")

'''
Основная функция
'''

def command_parser(*args, **kwargs):
    '''
    Функция берет на вход командную строку и парсит ее содержимое.
    Затем запускает соответствующую функцию из custom_parser.py
    :param args:
    :param kwargs:
    :return:
    '''

    # Функции операций
    def tsv_parser(path: str = None, excluding: str = None):
        '''

        :param path:
        :param excluding:
        :return:
        '''
        passes = []
        for i, root, dirs, files in enumerate(os.walk(path)):
            for filename in files:
                if 'tsv' in filename and excluding not in filename:
                    tsv_path = os.path.join(root, filename)
                    #new_file_name: f'discovered_file_{i}.tsv')
                    passes.append(tsv_path)
        return passes


    def date_parser(path: str = None, date):
        '''

        :param path:
        :param date:
        :return:
        import os

def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime
        '''
        passes = []
        for root, dirs, files in os.walk(path):
            for filename in files:
                date_path = os.path.join(root, filename)
                if 'tsv' in tsv_path and excluding not in tsv_path:
                    passes.append(tsv_path)
        return passes

    def diff_txt(file_1: str = None, file_2: str = None):
        pass


    parser = argparse.ArgumentParser("Command parser")  # заводим основной парсер

    subparsers = parser.add_subparsers(dest='command', required=True)  # заводим основной подпарсер

    parser_add = subparsers.add_parser("add", help="sums two numbers")
    parser_add.add_argument("x", type=int, help='first number')
    parser_add.add_argument("y", type=int, help='second number')
    parser_add.set_defaults(func='add')

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
