import pytest
import datetime


@pytest.fixture
def start_end_time_log():
    start_time = datetime.datetime.now()
    print(f"\nВремя начала тестов: {start_time.strftime('%H:%M:%S')}")
    yield
    end_time = datetime.datetime.now()
    print(f"\nВремя окончания тестов: {end_time.strftime('%H:%M:%S')}")


@pytest.fixture
def time_log():
    start_time = datetime.datetime.now()
    yield
    end_time = datetime.datetime.now()
    exec_time = end_time - start_time
    return print(f"\nВремя выполнения теста: {exec_time} сек.")