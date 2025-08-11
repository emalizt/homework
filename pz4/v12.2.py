N = int(input("Введите число N которое больше 1: "))
sum = 0
k = 0
while sum + k <= N:
    k += 1
    sum += k
print(sum)
print(k)