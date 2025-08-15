def calc(num):
    num_1 = num ** 2
    num_2 = num ** 3
    num_3 = num ** 4
    return num_1, num_2, num_3

number = int(input("Введите число: "))
b, c, d = calc(number)

print("Вторая степень :", b)
print("Третья степень :", c)
print("Четвертая степень :", d)