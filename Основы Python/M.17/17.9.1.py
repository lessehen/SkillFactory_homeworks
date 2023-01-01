# Вначале определим функцию, которая проверяет, является ли числом то, что должно им являться.
# Её я честно нагуглила, потому что хотела работать с float, а встроенные методы, о которых знаю, проверяют только int.


def is_number(x):
    try:
        float(x)  #
        return True
    except ValueError:
        return False


# Далее запрашиваем у пользователя числовую последовательность:
input_str = input('Введите несколько чисел, отделяя их друг от друга пробелами\n'
                  '(при вводе десятичных дробей используйте точку для отделения дробной части от целой):\n')

# Превращаем строку в список (пункт 1 задания):
input_list = input_str.split()
# И с помощью функции проверяем, являются ли элементы списка числами:
for a in input_list:
    if not is_number(a):
        raise ValueError(f'Значение "{a}" не соответствует условиям ввода. Перезапустите программу.')
# Если всё в порядке, преобразуем элементы списка в float:
fl_list = list(map(float, input_list))

# Просим у пользователя ввести ещё одно число:
input_one = input('Введите одно число, для которого необходимо выполнить проверку:\n')
# Делаем проверку на число (если введено несколько чисел, то строка также не пройдёт проверку, что нам и нужно):
if not is_number(input_one):
    raise ValueError(f'Значение "{input_one}" не соответствует условиям ввода. Перезапустите программу.')
else:
    fl_one = float(input_one)


# Переходим к сортировке - объявляем функцию (копируем из модуля и стараемся не сломать)
def merge_sort(lst):  # разделяем массив
    if len(lst) < 2:  # если кусок массива равен 2,
        return lst[:]  # выходим из рекурсии
    else:
        middle = len(lst) // 2  # ищем середину
        left = merge_sort(lst[:middle])  # рекурсивно делим части
        right = merge_sort(lst[middle:])
        return merge(left, right)  # выполняем их слияние


def merge(left, right):  # функция слияния
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    while i < len(left) and j < len(right):  # пока указатели не вышли за границы
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):  # добавляем хвосты
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


sorted_fl_list = merge_sort(fl_list)  # Сортируем наш список
# print(sorted_fl_list)  # Чтобы проверить, что получилось

# Переходим к поиску:
def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


# Проверяем, что fl_one попадает в числовой диапазон от первого по последнего значения sorted_fl_list:
if sorted_fl_list[0] < fl_one <= sorted_fl_list[-1]:
    if fl_one not in sorted_fl_list:
        # Если число входит в диапазон, но не встречается в списке - добавляем, сортируем список и применяем поиск:
        sorted_fl_list.append(fl_one)
        final_list = merge_sort(sorted_fl_list)
        print(f'Индекс искомого элемента на программистском: '
              f'{(binary_search(final_list, fl_one, 0, len(final_list) - 1)) - 1};\n'
              f'номер элемента в бытовом понимании: {(binary_search(final_list, fl_one, 0, len(final_list) - 1))}.')
    else:  # Иначе - число уже есть в списке, работаем с sorted_fl_list:
        print(f'Индекс искомого элемента на программистском: '
              f'{(binary_search(sorted_fl_list, fl_one, 0, len(sorted_fl_list) - 1)) - 1}:\n'
              f'номер элемента в бытовом понимании: '
              f'{(binary_search(sorted_fl_list, fl_one, 0, len(sorted_fl_list) - 1))}.')
else:
    print(f'Нет решений, т. к. значение {fl_one} находится за пределами диапазона '
          f'({sorted_fl_list[0]}; {sorted_fl_list[-1]}].')
