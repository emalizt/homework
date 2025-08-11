N = int(input("Введите целое число: "))
x = 0
while N > 0:
    x = x * 10 + N % 10
    N = N // 10
print(x)