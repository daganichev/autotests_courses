# Задача со ЗВЁЗДОЧКОЙ. Решать НЕ обязательно.
# Программа получает на вход натуральное число num.
# Программа должна вывести другое натуральное число, удовлетворяющее условиям:
# Новое число должно отличаться от данного ровно одной цифрой
# Новое число должно столько же знаков как исходное
# Новое число должно делиться на 3
# Новое число должно быть максимально возможным из всех таких чисел
# Например (Ввод --> Вывод) :
#
# 379 --> 879
# 15 --> 75
# 4974 --> 7974

def max_division_by_3(num):
    save_value = num
    list_save_value = []
    step = 10 ** (len(str(num)) - 1)
    check = True
    i = 0
    while (step >= 1):
        while (check):
            if int(str(num)[i]) == 9:
                if num % 3 == 0:
                    list_save_value.append(num)
                num = save_value
                check = False
                i += 1
            elif num % 3 == 0:
                list_save_value.append(num)
            num += step
        step = step // 10
        check = True
        num = save_value
    new_num = max(list_save_value)
    return new_num

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ

data = [
    379, 810, 981, 4974, 996, 9000, 15, 0, 9881, 9984, 9876543210, 98795432109879543210
]

test_data = [
    879, 870, 987, 7974, 999, 9900, 75, 9, 9981, 9987, 9879543210, 98798432109879543210
]


for i, d in enumerate(data):
    assert max_division_by_3(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')