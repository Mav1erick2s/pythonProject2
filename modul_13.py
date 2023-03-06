#### 13. Операторы сравнения и логические операторы ####
# and - Результат применения оператора and будет истинным, если и первое, и второе являются истинными. Во всех остальных случаях результат — False (ложь).
# можно проверить, находится ли число 1 в промежутке (0,4)
# cond1 = 0 < 1
# cond2 = 1 < 4
# print(cond1 and cond2)
# # True

# или, например, содержат ли две строки один и тот же символ
# cond3 = 't' in "python"
# cond4 = 't' in "django"
# print(cond3 and cond4)

# or -  если хотя бы один является истинным, то и результат тоже будет истинным
# к слову, логические выражения можно сразу объединять в одно целое
# print(('t' in "python") or ('t' in "django"))
# True

# a= not False and True or False and not True
# print(a)

# def is_leap_year(x):
#     return ((x % 4 == 0) and (x % 100 != 0)) or (x % 400 == 0)
# print(is_leap_year(x=2008))


# >,<
# def is_correct_password(password):
#     length = len(password)
#     return length > 8 and length < 20
# print(is_correct_password("hjkkjfnwjfnjfw"))
# print(len('hjkkjfnwjfnjfw'))


# And, or - Задача про квартиру
# def is_good_apartment(area, street):
#     return (area >= 100) or (area >= 80 and street == 'Main Street')
#
# print(is_good_apartment(91, 'Queens Street'))  # => False
# print(is_good_apartment(78, 'Queens Street'))  # => False
# print(is_good_apartment(70, 'Main Street'))    # => False
#
# print(is_good_apartment(120, 'Queens Street'))  # => True
# print(is_good_apartment(120, 'Main Street'))    # => True
# print(is_good_apartment(80, 'Main Street'))     # => True


##################### задача  random
# def bulochka_you(a, b):
#     return (a > b) or (a % 2 == 0) and (b % 2 == 0)
#
# v = int(input("Введи число 'a': "))
# g = int(input("Введи число 'b': "))
# # print(bulochka_you(a, b))
#
# if bulochka_you(v,g):
#  print('Максим крутой')
# else:
#  print('не очень')

## Содержит ли строка число 9
# list_digit = list(map(int, ['1', '2', '3', '4', '5', '6', '7', '8', '9']))
# print(9 in list_digit)
# # а можно так
# print('9' in str(123456789))

# # If, else
# is_rainy = True  # дождь будет
# heavy_rain = False  # не сильный дождь
#
# if is_rainy:
#     # в данный блок дописали ещё один условный оператор
#     if heavy_rain:
#         print("Брать зонт")
#     else:
#         print("Надеть дождевик")
# else:
#     print("Не брать зонт")

## Чтобы проверить, к чему будет приведен тот или иной тип,  можете воспользоваться встроенной функцией bool:
# print(bool(0))  # False
# print(bool(1))  # True
#
# print(bool("")) # False
# print(bool("1"))  # True
#
# print(bool([])) # False
# print(bool([1]))  # True

## Если ваша задача проверить, можно ли делить, и является ли делитель нулём, то проверку в явном виде zero != 0 делать излишне
# zero=0
# if zero:
#    print(int(10 / zero))
# else:
#    print("Делить на ноль нельзя")

## Проверить является строка пустой иили нет
# password='karemrf23'
# if not password:
#    print("Вы забыли ввести пароль")
# else:
#    print('все ок')


### КОД ОТЛОВА
# try:
#     *ваш код*
# except Ошибка:
#     *Код отлова*
# else:
#     *Код, который выполнится, если всё хорошо прошло в блоке try*
# finally:
#     *Код, который выполнится в любом случае*


##Как же сделать так, чтобы программа не вылетала при ошибке и продолжала свою работу? Это очень просто. Для этого и нужна конструкция try-except.
# try:  # Добавляем конструкцию try-except для отлова нашей ошибки
#     print("Перед исключением")
#     # теперь пользователь сам вводит числа для деления
#     a = int(input("a: "))
#     b = int(input("b: "))
#     c = a / b  # здесь может возникнуть исключение деления на ноль
#     print(c)  # печатаем c = a / b если всё хорошо
# except ZeroDivisionError as e:  # Добавляем тип именно той ошибки которую хотим отловить.
#     print(e)  # Выводим информацию об ошибке
#     print("После исключения")
#
# print("После После исключения")


##Ну, конечно же, это ещё не всё. Есть также блоки finally и else.
# Если вы хорошо помните тему условия, то там тоже было ключевое слово else.
# Код в блоке else выполнялся после завершения цикла. С try-except есть нечто похожее.
# try:
#     print("Перед исключением")
#     a = int(input("a: "))
#     b = int(input("b: "))
#     c = a / b
#     print(c)  # печатаем c = a / b, если всё хорошо
# except ZeroDivisionError as e:
#     print("После исключения")
# else:  # код в блоке else выполняется только в том случае, если код в блоке try выполнился успешно (т.е. не вылетело никакого исключения).
#     print("Всё ништяк")
# finally:  # код в блоке finally выполнится в любом случае при выходе из try-except
#     print("Finally на месте")
#
# print("После После исключения")


###Мы можем вызывать ошибки самостоятельно с помощью конструкции raise
# age = int(input("How old are you?"))
#
# if age > 100 or age <= 0:
#     raise ValueError("Тебе не может быть столько лет")
#
# print(f"Тебе {age} лет!")  # Возраст выводится только в случае, если пользователь ввёл правильный возраст.

##
# try:
#     y = int(input('Введите число:\t'))
# except ValueError as e:
#     print('Вы ввели неправильное число')
# else:
#     print('Вы ввели', y)
# finally:
#     print('Выход из программы')

# A = int(input('Введите число: '))
# if A % 2 == 0 or A % 3 == 0:
#     print('Число А кратно 2 или 3')
# else:
#     print('Число A не кратно 2 или 3')


### 13.5.1
# def are_both_odd(A, B):
#     return (A % 2 != 0) and (B % 2 != 0)
# print(are_both_odd(A = 2, B = 4))


# hour = 10
# if hour >=6 and hour < 12:
#     print('morning')
#
# if 6 <= hour < 12:
#     print("Утро!!!")

 # x = int(input('x: '))
# x = 5
# y = int(input('y: '))
#
# if x > 0 and y > 0:
#     print('первая четверть')
# if x < 0 and y < 0:
#     print('третья четверть')
# if x > 0 and y < 0:
#     print('четвертая четверть')
# if x < 0 and y > 0:
#     print('вторая четверть')

