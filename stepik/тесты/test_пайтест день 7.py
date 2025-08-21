#функция возвращает словарь с данными пользователя. Создай фикстуру, которая возвращает. Тест должен проверить: id — число, name — непустая строка active — булево значение
import pytest
@pytest.fixture
def users():
    return {"id": 1, "name": "Alice", "active": True}

def test_users(users):
    assert isinstance(users["id"], int)
    assert isinstance(users["name"], str)
    assert users["name"] != ""
    assert isinstance(users["active"], bool)
