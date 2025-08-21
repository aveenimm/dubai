#Напиши тест, который проверяет, что число 10 больше 5.
def test_numb():
    assert 10>5
    
#апиши тест, который проверяет, что длина строки 'hello' равна 5.
def test_long():
    long = 'hello'
    assert len(long) == 5
    
#пиши тест, который проверяет, что сумма чисел [1, 2, 3] равна 6.
def test_numbers():
    numbers = [1, 2, 3]
    assert sum(numbers) == 6

#апиши тест, который проверяет, что максимальное число в списке [3, 7, 2, 9, 4] равно 9.
def test_numbers():
    numbers = [3, 7, 2, 9, 4]
    assert max(numbers) == 9

#апиши тест, который проверяет, что слово 'test' начинается с буквы 't'.
def test_word():
    word = 'test'
    assert word [0] == 't'

# Дано число n. Проверь, что оно больше нуля.
def test_numbers():
    n = 5
    assert n > 0

# Дана строка word. Проверь, что её длина равна 7.
def test_alphabet():
    alpha = 'word'
    assert len(alpha) == 4

# Дано число x. Проверь, что оно чётное.
def test_numbers():
    x = 2
    assert x % 2 == 0

# Дана строка name. Проверь, что она начинается с заглавной буквы.
def test_name():
    name = 'Ivan'
    assert name [0] == 'I'

# Дан список чисел numbers. Проверь, что все числа положительные.
def test_numbers():
    numbers = [1, 2, 4]
    for i in numbers:
        assert i > 0

# Дан список чисел nums. Проверь, что сумма всех чисел равна 100.
def test_nums():
    nums = [50, 50]
    assert sum(nums) == 100

# Дан список чисел data. Проверь, что максимальный элемент равен 999.
import pytest
@pytest.mark.smoke #тут маркировка запуск через pytest -m smoke
def test_data():
    data = [0, 8, 78, 999]
    assert max(data) == 999

# Проверь, что строка email содержит символ "@" и символ ".", причём "@" находится в строке раньше ".".
def test_eamil():
    email = 'jopabobra@cobra.sru'
    assert '@' in email
    assert '.' in email
    assert email.index('@') < email.index('.')
