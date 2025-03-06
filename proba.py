'''Импорты
'''
import sys
import os
import glob
import pathlib
from pathlib import Path
from datetime import date
a, b, c = map(int, input('Введите дату в формате YYYY MM DD: ').split())
data = date(a, b, c)
path = input('Введите путь: ')
typef = 'tsv'
except_string = {'parcel', 'checkpoint'}

''' 
Рабочая часть
'''
real_path = Path(path)
''' Проверка того, что путь существует - сделать!!!!!!!!!!!!!!
'''
os.chdir(path)
try:
    os.mkdir('parsing_result')
except:
    pass

result = os.path.join(path, 'parsing_result', 'result_'+ typef+'.tsv')
print(result)
except_flag = False
with open(result, 'w') as res_file:
    for root, dirs, files in os.walk(real_path):
        for filename in files:
            for string in except_string: # ищем исключения
                if string in filename:
                    except_flag = True
                    break


            if except_flag or '.' not in filename or typef not in filename:
                continue
            try:
                new_path = os.path.join(root, filename)
                if date:
                    get_date = os.path.getmtime(new_path)
                    if get_date is date:
                        res_file.write(os.path.join(root, filename)+'\n') # запись пути в результирующий файл
                else:
                    res_file.write(os.path.join(root, filename) + '\n')
            except:
                raise PermissionError (f'Приложение не может получить доступ к файлу')
print('Выполнено. Файл, содержащий пути к найденным файлам, тут:', result)