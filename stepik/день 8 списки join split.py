# Пользователь вводит строку с несколькими словами через пробел. Выведи каждое слово на новой строке.
print('\n'.join(input().split()))

# вывести каждое слово на новой строке.
word = 'hello world python'
print('\n'.join(word.split()))

# вывести через запятую
word = 'apple banana cherry'
print(', '.join(word.split()))

# Разбей строку на список слов и выведи его.
word = "python java c++"
print(word.split())