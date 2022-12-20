# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

my_list = [2, 5, 2, 2, 7, 9, 10, 3]
result = []
my_list_length = len(my_list)

for i in range(int(my_list_length/2) + 1):

    if i == (my_list_length/2):

        if my_list[i] == int(my_list_length/2):
            result.append(my_list[i]**2)

    elif i == (my_list_length/2) + 0.5:

        if my_list[i] == int(my_list_length/2):
            result.append(my_list[i]**2)

    else:
        result.append(my_list[i]*my_list[my_list_length-1-i])

print(result)
