"""считает сумму и кол-во чисел в числе"""
N = int(input("Введите целое число: "))
num = 0
sum_num = 0
count = 0
while N > 0:
    num = N % 10
    N = N // 10
    sum_num += num
    count += 1
    print(num)
print(sum_num)
print(count)