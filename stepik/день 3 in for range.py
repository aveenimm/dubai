# Напишите программу, которая считывает одну строку, после чего выводит «YES» (без кавычек), если во введённой строке есть подстрока «синий», или «NO» (без кавычек) в противном случае.
name = input()
if 'синий' in name:
    print('YES')
else:
    print('NO')

# Напишите программу, которая считывает одну строку, после чего выводит «YES» (без кавычек), если во введённой строке есть подстрока «суббота» или «воскресенье», или «NO» (без кавычек) в противном случае.
chill = input()
if 'суббота' in chill or 'воскресенье' in chill:
    print('YES')
else:
    print('NO')

# Напишите программу, которая выводит текст «Python is awesome!» (без кавычек) 10 раз.
for i in range(10):
    print('Python is awesome!')

# Напишите программу, которая использует ровно три цикла for
for first in range(6):
    print('AAA')
for second in range(5):
    print('BBBB')
print('E')
for three in range(9):
    print('TTTTT')
print('G')

# Дано предложение и количество раз, сколько его надо повторить. Напишите программу, которая повторяет данное предложение нужное количество раз.
i = input()
numer = int(input())
for _ in range(numer):
    print(i)

# Напишите программу, которая считывает одну строку текста и выводит 10 строк, пронумерованных от 0 до 9 каждая, с указанной строкой текста.
name = input()
for i in range(10):
    print(i, name)

#На вход программе подаётся натуральное число апишите программу, которая для каждого из чисел от 0 до n (включительно) выводит текст
n = int(input())
for i in range(n+1):
    print(f'Квадрат числа {i} равен {i*i}')

#Даны два целых числа m и n (m≤n). Напишите программу, которая выводит все целые числа от m до n включительно.
m = int(input())
n = int(input())
for i in range(m, n+1):
    if m <= n:
        print(i)

#Запроси у пользователя число. Если оно больше 0, выведи "Positive", если меньше 0 — "Negative", иначе "Zero"
numbers = int(input())
if numbers > 0:
    print('Positive')
elif numbers < 0 :
    print('Negative')
else:
    print('Zero')

#Даны два целых числа и n Напишите программу, которая выводит все целые числа от m до n включительно в порядке возрастания, если m<n, или в порядке убывания в противном случае.
m, n = int(input()), int(input())
for i in range(m,n+1):
    if m < n:
        print(i)
for i in range(m, n - 1, -1):
        print(i)

##Запроси у пользователя число. Если оно больше 0, выведи "Positive", если меньше 0 — "Negative", иначе "Zero"
numbers = int(input())
if numbers > 0:
    print('Positive')
elif numbers < 0 :
    print('Negative')
else:
    print('Zero')

#Дана переменная age. Если возраст меньше 18 — выведи "Access denied", иначе "Access granted".
age = int(input())
if age < 18:
    print('Access denied')
else:
    print('Access granted')

#Дана строка "Hello". Выведи каждый символ этой строки в новой строке, используя for.
a = 'Hello'
for i in a:
    print(i)
#Дано число N. Выведи все числа от 1 до N включительно.
n = int(input())
for i in range(1, n+1):
    print(i)