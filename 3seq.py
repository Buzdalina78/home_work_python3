# Модуль3
# Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
# Затем он вводит элементы 2-го списка
# Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
# Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
# Введите элементы 2-го списка: 2,5
# Результат: 1,3,4

str_number = input('Введите числа через запятую ')
numbers = str_number.split(',')
str_number = input('Введите числа через запятую ')
second_numbers = str_number.split(',')
print(numbers)
print(second_numbers)
for number in numbers[:]:
    if number in second_numbers:
        numbers.remove(number)
print(numbers)