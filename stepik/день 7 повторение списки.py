# Пользователь вводит 5 чисел через input() (по одному за раз). Сохрани их в список.Создай новый список, куда добавь только чётные числа из первого списка.Выведи новый список.
a, b, c, x, y = input(), input(), input(), input(), input()
s = [int(a), int(b), int(c), int(x), int(y)]
piska = []
for i in s:
    if i % 2 == 0:
        piska.append(i)
print(piska)

# Пользователь вводит название блюда из списка ["soup", "pizza", "salad"], если блюда нет — выводится сообщение об отсутствии, если есть — добавляется в список заказов, цикл продолжается до ввода "stop", после чего выводится итоговый список.
s = ["soup", "pizza", "salad"]
x = []
while True:
    a = input()
    if a == "stop":
        break
    elif a in s:
        x.append(a)
    else:
        print('no')
print(x)

# На вход программе подаётся 5 чисел. Создай список этих чисел и выведи только чётные.
a, b, c, x, u = int(input()), int(input()), int(input()), int(input()), int(input())
y = [a, b, c, x, u]
for i in y:
    if i % 2 == 0:
        print(i)    

# Пользователь вводит название книги. Если книга есть — вывести "Книга найдена" Если нет — "Книги нет"
books = ["Гарри Поттер", "Властелин колец", "Фриерен"]
book_name = input()
if book_name in books:
    print('Книга найдена')
else:
    print('Книги нет')

# Пользователь вводит одну заглавную букву русского алфавита.Вывести следующую букву.Если буква последняя (Я) — вывести "Дальше букв нет".
users = input().upper()
if users == 'я':
    print('Дальше букв нет')
else:
    print(users.upper())

# response = {
 #   "username": "Anna",
  #  "status": "active",
   # "role": "admin"
#}
#Если status не "active" → вывести "Пользователь заблокирован".Если role не "admin" → вывести "Доступ запрещён".Если всё ок → вывести "Доступ разрешён".
for i in response:
    if i ['status'] != 'active':
        print('Пользователь заблокирован')
    elif i ['role'] != 'admin':
        print('Доступ запрещён')
    else:
        print('Доступ разрешён')