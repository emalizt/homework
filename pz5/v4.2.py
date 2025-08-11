def RectPS(x1,y1,x2,y2):
    a = abs(x1 - x2)
    b = abs(y1 - y2)
    P = 2 * (a + b)
    S = a * b
    return P, S
x1 = int(input("Введите координату x1: "))
y1 = int(input("Введите координату y1: "))
x2 = int(input("Введите координату x2: "))
y2 = int(input("Введите координату y2: "))
P, S = RectPS(x1,y1,x2,y2)
print(P)
print(S)