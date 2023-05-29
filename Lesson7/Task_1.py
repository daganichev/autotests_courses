# Напишите класс Segment
# Для его инициализации нужно два кортежа с координатами точек (x1, y1), (x2, y2)
# Реализуйте методы класса:
# 1. length, который возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
# 2. x_axis_intersection, который возвращает True, если отрезок пересекает ось абцисс, иначе False
# 3. y_axis_intersection, который возвращает True, если отрезок пересекает ось ординат, иначе False
# Например (Ввод --> Вывод) :
# Segment((2, 3), (4, 5)).length() --> 2.83
# Segment((-2, -3), (4, 5)).x_axis_intersection() --> True
# Segment((-2, -3), (-4, -5)).y_axis_intersection() --> False

# Здесь пишем код

class Segment:
    def __init__(self, point_first, point_second):
        self.x_a, self.y_a = point_first
        self.x_b, self.y_b = point_second

    # Следующий метод высчитывает длину между двумя точками
    def length(self):
        line_length = ((self.x_b - self.x_a) ** 2 + (self.y_b - self.y_a) ** 2) ** 0.5
        return round(line_length, 2)

    # Следующий метод высчитывает, пересекает ли отрезок из двух точек ось х
    def x_axis_intersection(self):
        if self.y_a <= 0 <= self.y_b or self.y_a >= 0 >= self.y_b:
            return True
        return False

    # Следующий метод высчитывает, пересекает ли отрезок из двух точек ось у
    def y_axis_intersection(self):
        if self.x_a <= 0 <= self.x_b or self.x_a >= 0 >= self.x_b:
            return True
        return False

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection
        ]


test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
