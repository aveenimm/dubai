import pytest
# Проверить, есть ли в словаре ключ "age" и значение больше 18
user = {"name": "Alice", "age": 25, "active": True}


def test_user():
    assert 'age' in user
    assert user['age'] > 18

# Увеличь количество "banana" на 1 и добавь ключ "pear" со значением 5.


def test_update_words():
    words = {"apple": 2, "banana": 3, "orange": 1}
    words["banana"] += 1
    words["pear"] = 5
    assert words["banana"] == 4
    assert words["pear"] == 5


# Выведи значение по ключу "retries", если такого ключа нет — верни 0.
config = {"timeout": 30}


def test_con():
    assert 'retries' in config
    if 'retries' not in config:
        return 0

# Сделать класс, который объединяет тесты по студентам. Сделать фикстуру, которая отдаёт текущего студента для теста. Сделать тест с параметризацией, который проверяет, что балл студента не меньше 60.


class Teststudents:
    @pytest.fixture
    def students():
        students = [
            ("Alice", 85),
            ("Bob", 72),
            ("Charlie", 90),
            ("Diana", 65)
        ]
    return [0]


@pytest.mark.parametrize('shit', students, [
    ("Alice", 85),
    ("Bob", 72),
    ("Charlie", 90),
    ("Diana", 65)
])
def test_pampam(shit):
    assert
