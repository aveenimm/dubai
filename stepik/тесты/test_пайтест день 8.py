import pytest
# Напиши тест с параметризацией, который проверяет, что заданные строки являются палиндромами. "level", "radar", "world", "madam", "python"
@pytest.mark.parametrize('x', ["level", "radar", "world", "madam", "python"])

def test_pizda(x):
    assert x == x [::-1]

# Сделай тест с параметризацией, который проверяет, что возраст пользователя (в годах) попадает в допустимый диапазон от 18 до 60 включительно. 18, 25, 60, 17, 61, 30
@pytest.mark.parametrize('age', [18, 25, 60, 17, 61, 30])

def test_age(age):
    assert 18 <= age <= 60

# Проверить, что числа из списка являются чётными.
@pytest.mark.parametrize('numers', [2, 3, 4, 7, 10])

def test_numers(numers):
    assert numers % 2 == 0

#Проверить, что сумма a + b равна expected.
@pytest.mark.parametrize('a, b, expected', [
    (1, 2, 3),
    (5, 7, 12),
    (10, -2, 8)
    ])
def test_sum(a, b, expected):
    assert a  + b == expected

# Проверить, что слово читается одинаково слева направо и справа налево.
@pytest.mark.parametrize('word', ["level", "radar", "world", "madam", "python"])

def test_word(word):
    assert word == word[::-1]

# Длина слова равна length. Слово состоит только из маленьких букв.
@pytest.mark.parametrize('word, length', [
    ("apple", 5), 
    ("banana", 6),
    ("cat", 3)
    ])

def long_test(word, length):
    assert length == len(word)
    assert word == word.lower()

#Длина строки равна заданной. Строка начинается с буквы 'a'.Все буквы в нижнем регистре.
@pytest.mark.parametrize('x', ["apple", "ant", "anchor"])

def test_popa(x):
    assert len(x) > 0
    assert x.startswith('a')
    assert x == x.lower()

# Длина строки не меньше 4 символов.Строка заканчивается на букву 'e'. Все буквы в верхнем регистре.
@pytest.mark.parametrize('n', ["LOVE", "HYPE", "FIRE"])

def test_word(n):
    assert len(n) >= 4
    assert n.endswith('E')
    assert n == n.upper()

#лина строки ровно 6 символов. Строка начинается с буквы 'p'. В строке есть только буквы (нет цифр и символов).
@pytest.mark.parametrize('m', ["python", "puzzle", "people"])

def test_xui(m):
    assert len(m) == 6
    assert m.startswith('p')
    assert m.isalpha()

# Фикстура с набором слов
@pytest.fixture
def sample_words():
    return ["apple", "banana", "cat", "dog"]

@pytest.mark.parametrize('word', ["apple", "banana", "cat", "dog"])

def test_word(sample_words, word):
    assert word in sample_words
    assert len(word) > 2
    assert word == word.lower()

#Напиши тест, который проверяет Число есть в списке фикстуры Число больше 5. Число делится на 5 без остатка
@pytest.fixture
def xui():
    return [10, 15, 20, 25]

@pytest.mark.parametrize('numbers', [10, 15, 20, 25])

def test_popa(numbers, xui):
    assert numbers in xui
    assert numbers > 5
    assert numbers % 5 == 0

#Слово есть в списке фикстуры. Длина слова больше 3. Все буквы в слове не в верхнем регистре полностью (т.е. слово не должно быть полностью заглавными)
@pytest.fixture
def world_list():
    return ["Python", "pytest", "code", "test"]

@pytest.mark.parametrize('word', ["Python", "pytest", "code", "test"])

def test_xui(word, world_list):
    assert word in world_list
    assert len(word) > 3
    assert word != word.upper()