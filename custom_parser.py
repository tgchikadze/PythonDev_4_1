'''
Настоящий файл содержит все необходимые классы, методы и функции
для реализации функционала приложения
'''
import sys
import os
from pathlib import Path
import shutil
import platform
import pydantic

'''
Функции команд
1. Парсер файлов заданного типа
'''

def my_parser(typef: str = None, date: str = None, path: str = None, excluding: set = None):
    '''
    Функция принимает на вход путь к каталогу, в котором отыскивает все файлы указанного пользователем типа
    и возвращает пути к ним в tsv-файле по относительной ссылке '\parsing_result\result_tsv.tsv'.
    При запуске можно указать исключения в виде подстроки, которой не должно быть в имени файла.
    В случае, если путь не указан, функция ищет файлы нужного типа в той локальной папке, из которой запущено приложение.

    :param typef: str = None
    :param path: str = None
    :param excluding: str = None
    :return: passes: list, в случае, если требуемые файлы не найдены — пустой list.
    '''

    if typef == None and date == None:
        raise ValueError("Недостаточно параметров: для вызова функции my_parser: \
            необходимо указать либо тип искомого файла, либо дату последнего изменения, \
            либо и то, и другое")
    elif type(typef) != str or type(date) != str or type(path) != str or type(excluding) != str:
        raise TypeError("Как минимум один из аргуметов не является строкой")


    '''
    Возможные проблемы (обработать исключения или прикрутить pydantic):
    1. Не найден путь
    2. Неправильный тип файла +
    3. Дата не в том формате
    4. Один или несколько параметров имеют тип, отличный от строки +
    5. Проблемы с записью файла +
    
    '''
    passes = []
    for i, root, dirs, files in enumerate(os.walk(path)):
        for filename in files:
            if '.' not in filename or typef not in filename:
                continue

            if typef is filename.split('.')[-1] and excluding not in filename:
                try:
                    full_path = os.path.join(root, filename)  # !!!! Протестировать
                    passes.append(full_path)
                except:
                    continue

    return passes


'''
2. Копировщик найденных файлов в заданную директорию
'''


def my_copier(passes_file: str, path_to: str = None, excluding: str = None):
    '''
    Функция берет на вход список путей и обходит их, копируя файлы в заданную пользователем папку
    :param passes:
    :param path:
    :param excluding:
    :return:
    '''


def my_renamer(path: str = None, date):
    '''

    :param path:
    :param date:
    :return:
    import os


