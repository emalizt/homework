N = int(input("Введите целое число: "))
num = 0
while N > 0:
    num = N % 10
    N = N // 10
    print(num)
