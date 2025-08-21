import pytest
# есть ключ "price" значение price больше 0 ключ "in_stock" существует и его значение True
@pytest.mark.parametrize('product', [ 
{"name": "Laptop", "price": 1200, "in_stock": True}
])

def test_users(product):
    assert 'price' in product
    assert product['price'] > 0
    assert 'in_stock' in product
    assert product['in_stock'] == True

#все числа больше 0. Есть число 10
@pytest.mark.parametrize('spisok', [3, 5, 7, 10])

def test_lala(spisok):
    assert spisok > 0
    assert 10 in [3, 5, 7, 10]

# Строка содержит подстроку "PyTest". Длина строки больше 5. Строка начинается с заглавной буквы 
text = "PyTest is cool"
@pytest.mark.parametrize('xui', ['PyTest is cool'])

def test_pisa(xui):
    assert 'PyTest' in xui
    assert len(xui) > 5
    assert xui[0].isupper()

# Все числа чётные или нечётные по условию: если число делится на 2 → чётное. Если число больше 10 → должно быть нечётным

nums = [2, 4, 7, 10, 13]
@pytest.mark.parametrize('num', nums)
def test_numbers(num):
    if num > 10:
        assert num % 2 != 0  
        if num % 2 == 0:
            assert True  
        else:
            assert True 

# Длина слова больше 4 Если слово начинается с заглавной буквы → длина слова больше 5
words = ["apple", "Banana", "cherry", "Date"]
@pytest.mark.parametrize('word', words)

def test_pisa(word):
    assert len(word) > 4
    if word[0].isupper():
        assert len(word) > 5

# Все слова длиной больше 4. Если слово начинается с заглавной буквы — длина больше 5
fruits = ["apple", "Banana", "cherry", "Date", "Elderberry"]

@pytest.mark.parametrize('negr', fruits)

def test_bla(negr):
    assert len(negr) > 4
    if negr[0].isupper():
        assert len(negr) > 5

# у каждого пользователя должно быть поле "name". Если возраст больше 18 — "active" должно быть True
@pytest.mark.parametrize('pizda', [
    {"name": "Alice", "age": 25, "active": True},
    {"name": "Bob", "age": 17, "active": False},
    {"name": "Charlie", "age": 30, "active": True}
])
 
def test_pam(pizda):
    assert 'name' in pizda
    if pizda['age'] > 18:
        assert pizda['active'] == True

#У каждого элемента должно быть поле "price" и оно больш 50. Если "in_stock" равно True — цена должна быть больше 50
items = [
    {"product": "Laptop", "price": 1200, "in_stock": True},
    {"product": "Mouse", "price": 25, "in_stock": False},
    {"product": "Keyboard", "price": 100, "in_stock": True}
]
@pytest.mark.parametrize('zhopa', items)

def test_da(zhopa):
    assert 'price' in zhopa
    assert zhopa['price'] > 50
    if zhopa['in_stock'] == True:
        assert zhopa['price'] > 50

#Все числа больше 0. Если число больше 10 — оно должно быть нечётным
numbers = [2, 5, 8, 11, 14]
@pytest.mark.parametrize('popa', numbers)

def test_pizda(popa):
    assert popa > 0
    if popa > 10:
        assert popa % 2 != 0

# Все слова содержат букву "a". Если слово начинается с заглавной буквы — длина слова больше 5
words = ["apple", "Banana", "cherry", "Date", "Elderberry"]
@pytest.mark.parametrize('opa', words)

def test_ep(opa):
    assert 'a' in opa
    if opa[0].isupper():
        assert len(opa) > 5

#У каждого товара есть поле "price" и оно больше 0. Если "stock" больше 0 — цена должна быть больше 50
products = [
    {"name": "Laptop", "price": 1200, "stock": 5},
    {"name": "Mouse", "price": 25, "stock": 0},
    {"name": "Keyboard", "price": 100, "stock": 10}
]
@pytest.mark.parametrize('gavno', products)

def test_pu(gavno):
    assert 'price' in gavno
    assert gavno['price'] > 0
    if gavno['stock'] > 0:
        assert gavno['price'] > 50

# Если элемент — число, оно должно быть больше 0. Если элемент — строка, её длина должна быть больше 3
data = [2, "apple", 7, "Banana", 12]

@pytest.mark.parametrize('aga', data)

def test_gg(aga):
    if isinstance(aga, int):
        assert aga > 0
    else:
        assert len(aga) > 3

# Если элемент — число → должно быть больше 0. Если элемент — строка → длина больше 4. Если элемент — словарь → должно содержать ключ "name" и "age"
mixed = [
    5,
    "Hello",
    {"name": "Alice", "age": 25},
    12,
    "Python",
    {"name": "Bob", "age": 17}
]
@pytest.mark.xuila
@pytest.mark.parametrize('p', mixed)

def test_d(p):
    if isinstance(p, int):
        assert p > 0
    elif isinstance(p, str):
        assert len(p) > 4
    else:
        assert p['name']
        assert 'age' in p
        
