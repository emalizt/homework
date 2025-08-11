"""
считает A в степени N и перемножают числа A
"""
A = int(input("Введите число A: "))
N = int(input("Введите число N: "))
sum = 0
x = 1
for i in range(0, N + 1):
    sum += x
    print(x)
    x *= A
print(sum)