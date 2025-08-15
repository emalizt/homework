def Minmax(x, y):
    minimum = min(x, y)
    maximum = max(x, y)
    return minimum, maximum

A = int(input("Введите число: "))
B = int(input("Введите  число: "))
C = int(input("Введите  число: "))
D = int(input("Введите  число: "))

minimum_AB, maximum_AB = Minmax(A, B)
minimum_CD, maximum_CD = Minmax(C, D)
minimum_ABCD = min(minimum_AB, minimum_CD)
maximum_ABCD = max(maximum_AB, maximum_CD)
print(minimum_ABCD)
print(maximum_ABCD)