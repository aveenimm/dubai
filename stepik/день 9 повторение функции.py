# Выведи каждое слово в новой строке.
word = 'red green blue'
print('\n'.join(word.split()))

# Ввод: I love Python → вывести слова через один пробел (лишние пробелы убрать).
word = 'I love Python'
print(word.strip())

# Напишите функцию, которая выводит звёздный прямоугольник с размерами 14×10
def draw_box():
    print('*'*10)
    for i in range(12):
        print('*        *')
    print('*'*10)
draw_box()

# Напишите функцию,которая выводит звёздный прямоугольный треугольник с катетами, равными 10
def draw_triangle():
    for i in range(10):
        print("*" * (1 + i))
draw_triangle()

# Если число чётное, увеличить его на 10. Если число нечётное, оставить без изменений. В конце вывести новый список.
numbers = [1, 2, 3, 4, 5]
new_numbers = []
for i in numbers:
    if i % 2 == 0:
        i = i + 10
        new_numbers.append(i)
    else:
        new_numbers.append(i)
print(new_numbers)

#Нужно пройтись циклом по списку и создать новый список: если имя длиннее 3 букв → добавить его в верхнем регистре (большими буквами), если имя 3 буквы или меньше → добавить в нижнем регистре (маленькими буквами).
names = ["Anna", "Bob", "Alice", "Tom", "Eve"]
new_names = []
for i in names:
    if len(i) > 3:
        new_names.append(i.upper())
    else:
        new_names.append(i.lower())

# если число положительное → добавить в новый список число, умноженное на 2, если число отрицательное → добавить в новый список число в виде строки (str()), если число равно 0 → добавить слово "ZERO".
numbers = [3, -5, 12, 0, -7, 8]
new_numbers = []
for i in numbers:
    if i > 0:
        new_numbers.append(i*2)
    elif i < 0:
        new_numbers.append(str(i))
    else:
        new_numbers.append('ZERO')

# Если длина имени > 3 → добавить в новый список строку "VALID:<имя>" Если длина ≤ 3 → добавить "SHORT:<имя>"
users = ["Anna", "Bob", "Alice", "Tom", "Eve"]
new_users = []
for i in users:
    if len(i) > 3:
        new_users.append('VALID: ' + i)
    else:
        new_users.append('SHORT: ' + i)

    