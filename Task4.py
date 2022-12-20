# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

num = int(input("Введите десятичное число: "))
original_num = num
if (num < 0):
    num = abs(num)

remains = []

while num != 0:
    remains.append(num % 2)
    num //= 2

binary_code = []
for i in range(len(remains)-1, -1, -1):
    binary_code.append(remains[i])

if original_num < 0:

    for i in range(len(binary_code)):
        if binary_code[i] == 1:
            binary_code[i] = 0
        elif binary_code[i] == 0:
            binary_code[i] = 1

    binary_code.insert(0, 1)

    if binary_code[len(binary_code)-1] == 0:
        binary_code[len(binary_code)-1] = 1
    elif binary_code[len(binary_code)-1] == 1:
        binary_code[len(binary_code)-1] = 0

if original_num == 0:
    print(0)      
else:      
    print(*binary_code, sep='')