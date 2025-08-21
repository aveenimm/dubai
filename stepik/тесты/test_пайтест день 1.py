# Напиши функцию test_sum(), которая проверит, что сумма 3 и 5 равна 8.
def test_sum():
    assert 3 + 5 == 8

# Функция test_is_even() принимает число и проверяет, что оно чётное (делится на 2 без остатка).
def test_is_even():
    even = 2
    assert even % 2 == 0

# Если возраст < 18 — вернуть "Access denied", иначе — "Access granted".
def test_age():
    age = 18
    if age < 18:
        result = 'Access denied'
    else:
        result = 'Access granted'
    assert result == 'Access granted'

# Напиши функцию, которая принимает возраст и возвращает True, если возраст больше или равен 18, иначе False.
def test_age():
    age = 25
    if age >= 18:
        assert True
    else:
        assert False

# Напиши функцию, которая принимает имя пользователя (username) и возвращает True, если оно не пустое, иначе False.
def test_username():
    username = 'Ivan'
    assert username == 'Ivan'

# Функция принимает список товаров и возвращает True, если список не пустой, иначе False.
def test_fruits():
    fruits = ['apple', 'banana']
    assert fruits == ['apple', 'banana']

# Функция принимает пароль (строку) и возвращает True, если длина пароля больше или равна 8 символов, иначе False.
def test_password():
    password = 1234
    assert password == 1234

# Функция принимает число и возвращает True, если оно положительное, иначе False.
def test_numbers():
    numbers = 2
    assert numbers == 2

# Функция принимает имя пользователя и пароль, возвращает "Welcome" если username == "admin" и password == "12345", иначе "Access denied".
def test_name_password():
    name = 'admin'
    password = '12345'
    assert name == 'admin' and password == '12345'

# Функция принимает строку и возвращает True, если в ней есть слово "test". Напиши тест с одной строкой.
def test_line():
    light = 'xuesos'
    assert light == 'xuesos'
