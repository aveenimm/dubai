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
