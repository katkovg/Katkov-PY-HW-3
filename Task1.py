# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.

my_list = [25, 34, 78, 9, 738, 5, 4]
result = 0

for i in range(1, len(my_list), 2):
    result+=my_list[i]
    
print(result)
