import pytest
#Напиши фикстуру, которая возвращает список чисел [1,2,3]. Напиши тест, который проверяет, что сумма чисел равна 6.
@pytest.fixture
def karloson():
    return [1,2,3]

def test_malish(karloson):
    assert karloson == [1,2,3]

#Есть список пользователей. Нужно проверить, что функция возвращает только пользователей с возрастом ≥18.
@pytest.fixture
def users():
    return [
        {"name": "Masha", "age": 18},
        {"name": "Shaxid", "age": 16}
    ]

def test_users(users):
    adults = [user for user in users if user["age"] >= 18]
    assert adults == [{"name": "Masha", "age": 18}]

#Фикстура даёт число, тест проверяет, что оно чётное.
@pytest.fixture
def numbers():
    return 2

def test_numbers(numbers):
    assert numbers % 2 == 0

# В проекте есть “система бонусов” для пользователей.Каждый пользователь получает бонусные баллы.
# Нам нужно написать тесты, чтобы проверять условия начисления бонусов:
# Баллы не могут быть отрицательными.
# Баллы всегда меньше или равны 100.
# Баллы кратны 5.
@pytest.fixture
def bonus():
    return 25

def test_bonus(bonus):
    assert bonus >=0
    assert bonus <= 100
    assert bonus % 5 == 0

# Фикстура возвращает бонусные баллы, тест проверяет, что они <= 50.
@pytest.fixture
def bonus():
    return 27

def test_bonus(bonus):
    assert bonus <= 50

#Каждый пользователь получает бонусные баллы.Нужно проверить несколько условий одновременно:Бонус ≥ 0 Бонус ≤ 100 Бонус кратен 5
@pytest.fixture
def bonus():
    return 25

def test_bonus_system(bonus):
    assert bonus >= 0
    assert bonus <= 100
    assert bonus % 5 == 0