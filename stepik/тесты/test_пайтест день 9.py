# если возраст ≥ 18 → результат "ADULT:<имя>" если возраст < 18 → результат "MINOR:<имя>"
import pytest
@pytest.fixture
def users():
    return [("Anna", 25), ("Bob", 17), ("Alice", 30), ("Tom", 16)]

@pytest.mark.parametrize('name, age', [
    ("Anna", 25),
    ("Bob", 17),
    ("Alice", 30),
    ("Tom", 16)
])
def test_users(users):
    for name, age in users:
        if age >= 18:
            result = f'ADULT: {name}'
            expected = f'ADULT: {name}'
        else:
            result = f'MINOR: {name}'
            expected = f'MINOR: {name}'
        assert result == expected