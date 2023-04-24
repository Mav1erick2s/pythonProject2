
def input_():  ## Функция ввода чисел и проверки на одинаковые элементы
    numbers = list(map(int, input("Введите целые числа через пробел: ").split()))
    for i in range((len(numbers) - 1)):
        for j in range(i + 1, (len(numbers))):
            if numbers[i] == numbers[j]:
                print("Вы ввели одинаковые числа")
                numbers = list(map(int, input("Введите целые числа через пробел: ").split()))
    return numbers


def Sort_bubble(array): ## Функция сортировки
    length = len(array)
    for i in range(length):
        for j in range(0, length-i-1):
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return numbers

def binary_search(array, number, left, right):  ## Функция бинарного поиска индекса элемента в массиве
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == number:
        return middle
    elif number < array[middle]:
        return binary_search(array, number, left, middle - 1)
    else:
        return binary_search(array, number, middle + 1, right)

def num_(numbers, number):  ## Функция элемента, меньшего чем введенный пользователем
    for i in (Sort_bubble(numbers)): #а следующий за ним больший или равный ему
        if i < number:
            num = i
    return num

numbers = input_()
number = int(input("Введите любое число: "))
print("Массив введенных чисел: ", numbers)
print("Целое число: ", number)
left = 0
right = len(numbers) - 1

index = binary_search(numbers, num_(numbers,number), left, right)
element = numbers[index]
print("Отсортированный список целых чисел: ", Sort_bubble(numbers))
print("Индекс и элемент, меньший введенного пользователем а следующий за ним больший или равный ему: ", "[", index, "]", element )

