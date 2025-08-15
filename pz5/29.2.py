def Swap(x, y):
    return y, x

A = int(input("Введите число: "))
B = int(input("Введите число: "))
C = int(input("Введите число: "))
D = int(input("Введите число: "))

swap_AB = Swap(A, B)
swap_CD = Swap(C, D)
swap_BC = Swap(B, C)
print(swap_AB)
print(swap_CD)
print(swap_BC)