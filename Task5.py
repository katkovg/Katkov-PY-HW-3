# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число: '))
fibonacci = []

for i in range(0, n):
    if i == 0:
        fibonacci.append(1)
    elif i == 1:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

fibonacci_reversed = []

if n % 2 == 0:
    for i in range(-1, -len(fibonacci)-1, -1):
        if i % 2 !=0:
            fibonacci_reversed.append(-(fibonacci[i]))
        else:
            fibonacci_reversed.append(fibonacci[i])
elif n % 2 != 0:
    for i in range(-1, -len(fibonacci)-1, -1):
        if i % 2 ==0:
            fibonacci_reversed.append(-(fibonacci[i]))
        else:
            fibonacci_reversed.append(fibonacci[i])

for i in range(n+1):
    if i == 0:
        fibonacci.insert(0, 0)
    else:
        fibonacci.insert(0, fibonacci_reversed[len(fibonacci_reversed) - i])

print(fibonacci)