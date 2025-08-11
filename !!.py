N = int(input("Введите целое число: "))
sum_num = 0
for i in range(N, 2 * N + 1):
    sum_num += i ** 2
    print(i ** 2)
print(sum_num)
