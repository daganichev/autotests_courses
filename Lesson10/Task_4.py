# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


@pytest.mark.usefixtures("start_end_time_log")
class TestDiv:
    def all_division(*arg1):
        division = arg1[1]
        for i in arg1[2:]:
            division /= i
        return division

    def test_positive_1(self):
        assert self.all_division(100, 50) == 2

    def test_positive_2(self):
        assert self.all_division(10, -10) == -1

    def test_negative_1(self, time_log):
        with pytest.raises(ZeroDivisionError):
            self.all_division(99, 0)

    def test_positive_3(self):
        assert self.all_division(99999, 521, 10, -245) == -0.07834149398723021

    def test_negative_2(self):
        with pytest.raises(TypeError):
            self.all_division('a', 'b')