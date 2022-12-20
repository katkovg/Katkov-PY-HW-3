# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.

from decimal import *

my_list = [9.782, 1.23, 3, 4.596, 6.22, 2.123]
only_integer_numbers_list = []
only_fractional_parts_list = []

for number in my_list:
    only_integer_numbers_list.append(int(number))

for i in range(len(my_list)):

    n = (Decimal(f'{my_list[i]}') - Decimal(f'{only_integer_numbers_list[i]}'))

    if n != 0:
        only_fractional_parts_list.append(n)

print(max(only_fractional_parts_list) - min(only_fractional_parts_list))

