N = int(input("Введите целое число: "))
product = 1.0
c = 1
while c <= N:
    product *= 1.0 + 0.1 * c
    c += 1
print(product)