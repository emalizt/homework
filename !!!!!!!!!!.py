N = int(input("Введите целое число: "))
sum_num = 0
for i in range(1, N + 1):
    sum_num += 1 / i
    print(1 / i)
print(sum_num)