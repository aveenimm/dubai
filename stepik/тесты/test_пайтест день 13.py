#Есть список слов. Нужно проверить, какие слова являются палиндромами (читаются одинаково слева направо и справа налево).
import pytest
word = ["level", "radar", "world", "madam", "python"]
@pytest.mark.parametrize('popa', word)

def test_slova(popa):
    assert popa == popa [::-1]

# Нужно проверить, что длина слова совпадает с ожидаемой.
pisa = [
    ("apple", 5),
    ("banana", 6),
    ("cat", 3),
    ("python", 6),
    ("hi", 2)
]
@pytest.mark.parametrize('popa', pisa)
def test_schlen(popa):
    word = popa[0]     # слово
    length = popa[1]   # длина
    assert len(word) == length

