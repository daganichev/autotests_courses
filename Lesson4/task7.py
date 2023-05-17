# Напишите алгоритм, который берет список lst и перемещает все нули в конец, сохраняя порядок остальных элементов.
# Например (Ввод --> Вывод) :
# [1, 0, 1, 2, 0, 1, 3]  => [1, 1, 2, 1, 3, 0, 0]

def move_zeros(lst):
    iteration_zero = 0
    while iteration_zero < len(lst):
        if lst[iteration_zero] == 0:
            iteration_number = iteration_zero
            while iteration_number < len(lst):
                if lst[iteration_number] != 0:
                    lst[iteration_zero], lst[iteration_number] = lst[iteration_number], lst[iteration_zero]
                    break
                iteration_number += 1
        iteration_zero += 1


    return lst

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    [1, 2, 0, 1, 0, 1, 0, 3, 0, 1],
    [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9],
    [0, 0],
    [1, 9, 5, 4, 8, 2],
    []
]

test_data = [
    [1, 2, 1, 1, 3, 1, 0, 0, 0, 0],
    [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0],
    [1, 9, 5, 4, 8, 2],
    []
]


for i, d in enumerate(data):
    assert move_zeros(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')