
# hours=11
# minutes=58
# seconds=42
#
# print("%d:%d:%d" % (hours, minutes, seconds))
#
# letters = ['a', 'b', 'c', 'о']
# letters.append('f')
# print(letters)
# print(letters[0])
# print(len(letters))
# print(letters[len(letters)-1])
# letters.pop(0)
# print(letters)
#
# L = [6.3, 4.4, 5.5, 6.6]
# # печатаем сам объект map
# print(map(round, L)) # к каждому элементу применяем функцию округления
# # <map object at 0x7fd7e86eb6a0>
# # и результат его преобразования в список
# print(list(map(round, L)))
# # [3, 4, 6, 7]
#
# string = input("Введите числа через пробел:") # 1 1 2 3 5 8 13 21 34 55 например
# list_of_strings = string.split() # список строковых представлений чисел
# list_of_numbers = list(map(int, list_of_strings)) # список чисел
# print(sum(list_of_numbers[::3])) # sum() вычисляет сумму элементов списка
#
# # все операции - деление строки по пробелам, преобразование к числам
# # и приведение объекта map к типу список, можно делать в одной строке
# L = list(map(float, input().split()))
# # обмениваем первое и последнее число
# # с помощью множественного присваивания
# L[0], L[-1] = L[-1], L[0]
# # находим сумму и добавляем её в конец списка
# L.append(sum(L))
# print("Значение переменной L", L)
#
# person = {} # с помощью фигурных скобок можно создать словарь
# # словарь заполняется по принципу - ключ:объект (через двоеточие)
# person = {'name' : 'Ivan Petrov'}
# # в него можно также добавлять новые объекты по ключу
# person['age'] = 25
# person['email'] = 'ivan_petrov@example.com'
# person['phone'] = '8(800)555-35-35'
# print(person)
# # {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com', 'phone': '8(800)555-35-35'}
# print(person.keys())
# # dict_keys(['name', 'age', 'email', 'phone'])
# print(person.values())
# # dict_values(['Ivan Petrov', 25, 'ivan_petrov@example.com', '8(800)555-35-35'])
# print(person)
# # {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com', 'phone': '8(800)555-35-35'}
# person.pop('phone')
# print(person)
# # {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com'}
# d = {'day' : 22, 'month' : 6, 'year' : 2015}
# print("||".join(d.keys()))
#
#
# name = 'Алиса в стране чудес'
# author = 'Кэрролл'
# year = '1865'
# book={'title':str(name), 'author':str(author),'year':int(year)}
# print(book)
# # или с помощью импут как в уроках
# title = input("Введите название книги:")
# author = input("Введите фамилию автора:")
# year = int(input("Введите год издания:"))
# book = {'title' : title, 'author' : author, 'year' : year}
# print(book)
#
# # множество(set)
# L = [1,1,2,3,2]
# b = list(set(L))
# print(b)
# # [1,2,3]
# text = input("Введите текст:")
# unique = list(set(text))
# print("Количество уникальных символов: ", len(unique))
#
# L = ['a', 'b', 'c']
# print(id(L))
# L.append('d')
# print(id(L))



####Вебинар «Типы данных в Python»####
# import math
# a=(math.pow(2, 10))
# b=int(a)
# print(b)

#Сложение строк
# name= "Niga"
# fullname=" you"
# rty = name+fullname
# print(rty)

# Ввод символов, если пользователь вводит все с маленькой буквы: нижний и верхний регистр
# name = input("Введите ваше имя ")
# name_start = name[0].upper()
# name_end = name[1:].lower()
# ggg = name_start+name_end
# print(ggg)

# Подсчет символов в строке "ю" с помощью функции for i in ekn
# ekn = "Я люблюю танцевать"
# ttt = 0
# for i in ekn:
#     if i == "ю":
#         ttt = ttt+1
# print(ttt, "буквы 'ю' в данной строке")

#Проверка на вхождение in и not in
# a="Привет"
# b="Привет толя"
# print(a in b)

#\n - перенос на следущую строку
#print("hello\nworld")

#порядок по ключевым словам
# string="{s}, {e}, {f}".format(f="Аня", e="Коля", s="Саша")
# print(string)

# List - []
# numbers = [1,2,3,4,5, 'hello', True]
# print(numbers)
# people=['Bob', 'Oleg', 'Sonya']
# #append(item) - добавляем новый элемент
# new_person = people.append('Tanya')
# #insert(item) - добавляем новый элемент в список по индексу
# new_person_2 = people.insert(2, "Billi")
# print(people)

#Словари - {}
#dikt
# user = {1:'none', 2:'note', 3:'nonem'}
# key= 3
# if key in user:
#     user=user[key]
#     print(user)
# else:
#     print('элемент не найден')
#items - Пишет в слолбик ключ, значение
# user = {1:'none', 2:'note', 3:'nonem'}
# for key, value in user.items():
#     print(key, value)

#Множества set{}
#union
# user_1 = {'none', 'note', 'nonem'}
# user_2 = {'none', 'natasha', 'igor'}
# user_3 = user_1.union(user_2)
# print(user_3)
# #intersection
# user_4 = user_1.intersection(user_2)
# print(user_4)
# user_5 = user_1.difference(user_2)
# print(user_5)

