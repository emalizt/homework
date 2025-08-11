N = int(input("Введите целое число: "))
sum_num = 0
Sign = 1
for i in range(1, N + 1):
    x = 1 + i / 10
    sum_num += x * Sign
    print(x * Sign)
    Sign *= -1
print(sum_num)
