#На вход программе подаются две строки чисел через пробел. Найти общее между ними (пересечение). Найти разность первой строки минус вторая. Вывести два результата: Первая строка: общие числа, отсортированные по возрастанию, через пробел. Вторая строка: разность, отсортированная по возрастанию, через пробел.
a, b = input(), input()
a_set = set(map(int, a.split()))
b_set = set(map(int, b.split()))
sred = a_set & b_set        # пересечение
bebra = a_set - b_set        # разность
print(*sorted(sred))         # вывод пересечения через пробел
print(*sorted(bebra))        # вывод разности через пробел



site_a = "Alice Bob Carol Dave Eve"
site_b = "Bob Carol Frank Eve Grace"
# Найти пользователей, которые зарегистрированы на обоих сайтах. Найти пользователей, которые есть только на первом сайте. Проверить, что все имена состоят из букв.
users1 = set(site_a.split())
users2 = set(site_b.split())
ab_users = users1 & users2
ab_users1 = users1 - users2
assert all(name.isalpha() for name in users1)
assert all(name.isalpha() for name in users2)
# Вывести: Список общих пользователей, отсортированный по алфавиту. Список уникальных пользователей первого сайта, отсортированный по алфавиту.
print (*sorted(ab_users))
print(*sorted(ab_users1))
