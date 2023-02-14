import pandas as pd
import numpy as np
import csv

 
class Modules: # Работаем с классом просто потому что так удобнее грузить нашу таблицу во все функции сразу одной строчкой
    def __init__(a, file):
        a.file = file
 
    def save_table(a, value):
        output_directory = 'Macintosh HD⁩\\Users\\levkrasulin⁩\\Python⁩\\TableService-master⁩\\examples⁩/' + value
        directory = a.file
        frame = pd.read_csv(directory)
        frame.to_csv(output_directory)
 
    def get_rows_by_number(a, value, start, stop, copy_table):
        output_directory = r'' + 'Macintosh HD⁩\\Users\\levkrasulin⁩\\get_rows_by_number.' + value
        directory = a.file
        if copy_table == True:
            frame = pd.read_csv(directory)
            print(frame[start:stop + 1])
 
        elif copy_table == False:
            frame = pd.read_csv(directory)
            frame[start:stop + 1].to_csv(output_directory, index=False)
            print(frame[start:stop + 1])
 
    def get_rows_by_index(a, value, copy_table, **val):
        output_directory = r'' + 'Macintosh HD⁩\\Users\\levkrasulin⁩\\get_rows_by_index.' + value
        directory = a.file
        key = val.values()
        if copy_table == True:
            frame = pd.read_csv(directory)
            print(pd.concat([frame[key]], ignore_index=True))
        elif copy_table == False:
            frame = pd.read_csv(directory)
            frame[key].to_csv(output_directory, index=False)
            print(pd.concat([frame[key]], ignore_index=True))
 
    def get_column_types(a):
        directory = a.file
        frame = pd.read_csv(directory)
        print(frame.info(null_counts=False, memory_usage=False))
 
    def set_column_types(a, types_dict):
        directory = a.file
        frame = pd.read_csv(directory)
        if types_dict == 'int':
            frame_show = frame.select_dtypes(include=['int64'])
            print(frame_show.info(null_counts=False, memory_usage=False))
        elif types_dict == 'float':
            frame_show = frame.select_dtypes(include=['int64'])
            print(frame_show.info(null_counts=False, memory_usage=False))
        elif types_dict == 'bool':
            frame_show = frame.select_dtypes(include=['bool'])
            print(frame_show.info(null_counts=False, memory_usage=False))
        elif types_dict == 'str':
            frame_show = frame.select_dtypes(include=['object'])
            print(frame_show.info(null_counts=False, memory_usage=False))
        else:
            print('Введите тип значений')
 
    def get_values(a, column):
        directory = a.file
        frame = pd.read_csv(directory)
        if type(column) == str:
            print(frame[column])
        elif type(column) == int:
            column_index = frame.columns[column]
            print(frame[column_index])
 
    def get_value(a, column):
        directory = a.file
        frame = pd.read_csv(directory)
        if type(column) == str:
            print(frame[column])
        elif type(column) == int:
            column_index = frame.columns[column]
            print(frame[column_index])
 
    def set_values(a, values, column):
        directory = a.file
        frame = pd.read_csv(directory)
        if type(column) == str:
            frame.loc[:, column] = values
            print(frame)
        elif type(column) == int:
            column_index = frame.columns[column]
            frame.loc[:, column_index] = values
            print(frame)
 
    def set_value(a, values, column):
        directory = a.file
        frame = pd.read_csv(directory)
        if type(column) == str:
            frame.loc[:, column] = values
            print(frame)
        elif type(column) == int:
            column_index = frame.columns[column]
            frame.loc[:, column_index] = values
            print(frame)
 
    def print_table(a):
        directory = a.file
        frame = pd.read_csv(directory)
        pd.options.display.max_rows = len(frame)
        print(frame)
    
    def print_type(a, column):
        directory = a.file
        frame = pd.read_csv(directory)
        column_index = frame.columns[column]
        print(type(frame[column_index][1]))
           
   
    
if __name__ == "__main__":
    load = Modules(r'examples⁩\input.csv') # Загрузка нашего файла с таблицей в класс Modules
    print('Список функций:',
          '0 - save_table [Название файла]', # Сохранение файла
          '1 - get_rows_by_number([Начальная строка], [Конечная строка])', # Вывод таблицы из заданного интервала
          '2 - get_rows_by_index([Название колонки])', # Вывод столбца с заданной колонкой
          '3 - get_column_types() ', # Вывод кол-ва колонок в таблице и их тип
          '4 - set_column_types([Тип колонок (int, float, bool, str)]) ', # Вывод словаря в виде СТОЛБЕЦ:ТИП
          '5 - get_values([Название колонки]) ', # Вывод списка значений таблицы по имени столбца
          '6 - get_value([Номер колонки]) ', # Вывод списка значений таблицы по номеру столбца
          '7 - set_values([Номер колонки], [Значение])', # Изменение значений в таблице, а также последующий её вывод
          '8 - set_value([Номер колонки], [Значение])', # Изменение значений в таблице, а также последующий её вывод
          '9 - print_type([Номер столбца])', #Тип значений в столбце
          '10 - print_table()', # Вывод таблицы
          '11 - break program', sep='\n') # Выход
    while True: # Ниже идёт выполнение наших функций
        func = input('Введите номер функции: ')
        if func == '0':
            print('\nDEBUG: Выполнение функции save_table ниже:\n')
            name = input('Введите название новой таблицы: ')
            load.save_table(name)
            print('Файл сохранён под названием: ' + name)
        elif func == '1':
            print('\nDEBUG: Выполнение функции get_rows_by_number ниже:\n')
            name = 'get_rows_by_number.' + input('Введите желаемое расширение: ')
            load.get_rows_by_number(name, int(input('Введите начальную строчку: ')), int(input('Введите конечную строчку: ')), copy_table=False)
            print('\nНовая таблица сохранена под названием: ' + name)
        elif func == '2':
            print('\nDEBUG: Выполнение функции get_rows_by_index ниже:\n')
            name = input('Введите желаемое расширение: ')
            load.get_rows_by_index(name, copy_table=False, val=input('Введите название колонки в таблице которую нужно вывести: '))
            print('\nНовая таблица сохранена под названием: ' + name)
        elif func == '3':
            print('\nDEBUG: Выполнение функции get_column_types ниже:\n')
            load.get_column_types()
        elif func == '4':
            print('\nDEBUG: Выполнение функции set_column_types ниже:\n')
            load.set_column_types(input('Введите тип колонок: '))
        elif func == '5':
            print('\nDEBUG: Выполнение функции get_values ниже:\n')
            load.get_values(input('Введите название колонки для того чтобы вывести её табличные значения: '))
        elif func == '6':
            print('\nDEBUG: Выполнение функции get_value ниже:\n')
            load.get_value(int(input('Введите номер колонки для того чтобы вывести её табличные значения: ')))
        elif func == '7':
            print('\nDEBUG: Выполнение функции set_values ниже:\n')
            load.set_values(column = int(input('Введите номер колонки для изменения в ней всех значений: ')), values = input('Введите новое значение: '))
        elif func == '8':
            print('\nDEBUG: Выполнение функции set_value ниже:\n')
            load.set_value(column = int(input('Введите номер колонки для изменения в ней всех значений: ')), values = int(input('Введите новое значение (только цифры): ')))
        elif func == '9':
            print('\nDEBUG: Выполнение функции print_type ниже:\n')
            load.print_type(int(input('Введите номер столбца, чтобы узнать тип его значений: ')))
        elif func == '10':
            print('\nDEBUG: Выполнение функции print_table ниже:\n')
            load.print_table()
        elif func == '11':
            print('\nDEBUG: BREAK')
            break
        else:
            print('\nТакого номера нет в списке, либо вы отправили пустое значение.')