import pytest
# Все id уникальные. У заказов со статусом PAID сумма (amount) всегда больше 0. Статус заказа всегда один из: "NEW", "PAID", "CANCELLED".
@pytest.fixture
def orders(): 
    return [
    {"id": 1, "status": "NEW", "amount": 100},
    {"id": 2, "status": "PAID", "amount": 250},
    {"id": 3, "status": "CANCELLED", "amount": 50},
    {"id": 4, "status": "PAID", "amount": 300}
]

@pytest.mark.parametrize('xz',[
{"id": 1, "status": "NEW", "amount": 100},
{"id": 2, "status": "PAID", "amount": 250},
{"id": 3, "status": "CANCELLED", "amount": 50},
{"id": 4, "status": "PAID", "amount": 300}
])

def test_omg(orders, xz):
    assert xz in orders
    allowed_statuses = ["NEW", "PAID", "CANCELLED"]
    assert xz['status'] in allowed_statuses
    if xz["status"] == "PAID":
        assert xz["amount"] > 0

# "name" есть в словаре. возраст больше 18
user = {"name": "Alice", "age": 25, "active": True}
def test_user(user):
    assert 'name' in user
    assert user ['age'] >= 18

#
