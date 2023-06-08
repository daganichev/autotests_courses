# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest



def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_positive_1():
     assert all_division(100, 50) == 2


def test_positive_2():
    assert all_division(10, -10) == -1

@pytest.mark.smoke
def test_negative_1():
    try:
        all_division(99, 0)
    except ZeroDivisionError:
        print(' Переданы неверные параметры', end='')


def test_positive_3():
    assert all_division(99999, 521, 10, -245) == -0.07834149398723021

def test_negative_2():
    try:
        all_division('a', 'b')
    except TypeError:
        print(' Переданы неверные параметры', end='')


