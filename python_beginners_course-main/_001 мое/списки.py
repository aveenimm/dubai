fruits = ['apple', 'banana', 'cherry']
print('fruits')

word = 'hello'
my_list = list(word)
print(my_list)

my_list1 = [1, 2, 3]
my_list2 = [3, 4, 5]
my_list3 = [6, 7, 8]
print(my_list1 + my_list2 + my_list3)

fruits = ['apple', 'banana', 'cherry']
fruits.append('watermellon')
print(fruits)

fruits = ['apple', 'banana', 'cherry'] 
fruit = fruits.pop()  # метод удаляе ластовое значение
print(fruit)  # вывод уделенного
print(fruits)  # вывод в итоге как получилось

fruits = ['apple', 'banana', 'cherry']
fruits2 = ['fig', 'grape']
fruits.extend(fruits2)  # добавилось второй список к первому (объединились)
print(fruits)

my_list = [5, 6, 10, 2, 34, 12]
my_list.sort()  # в выводе сортировка по порядку по возрастанию
print(my_list)

my_list = [5, 6, 10, 2, 34, 12]
my_list.sort(reverse=True)  # в выводе сортировка назад (по убыванию)
print(my_list)

my_list = [5, 6, 10, 2, 34, 12]
print(max(my_list)) # максимально в списке

