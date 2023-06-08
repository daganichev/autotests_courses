# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет.
# Реализовать без подключения новых модулей и сторонних библиотек.


import datetime
import time
from pathlib import Path

# Здесь пишем код


def func_log(file_log='log.txt'):
    """
    Функция принимает в параметры файл для логирования, если не задан, использует файл по умолчанию. Вызывает декоратор
    и записываем имя функции, дату и время в файл для логирования
    :param file_log: текстовый документ для логирования
    """
    def time_log(func):
        def wrapper():
            name_func = func.__name__
            date_time_func = datetime.datetime.now().strftime("%d.%m %H:%M:%S")
            with open(Path(Path.cwd(), 'test_file', f'{file_log}'), 'a', encoding='utf-8') as file_for_log:
                func()
                file_for_log.write(f'{name_func} вызвана {date_time_func}\n')
        return wrapper
    return time_log

@func_log()
def func1():
    time.sleep(3)


@func_log(file_log='func2.txt')
def func2():
    time.sleep(5)


func1()
func2()
func1()
