# def SortDec3(A, B, C):
#     max3 = max(A, max(B, C))
#     min3 = min(C, min(B, A))
#     minmax = A
#     if minmax == min3 or minmax == max3:
#         minmax = B
#     if minmax == min3 or minmax == max3:
#         minmax = C
#     return min3, minmax, max3
# A = int(input("Введите число: "))
# B = int(input("Введите число: "))
# C = int(input("Введите число: "))
# print(SortDec3(A, B, C))
def SortDec3(A, B, C):
    if A < B:
        A, B = B, A
    if A < C:
        A, C = C, A
    if B < C:
        B, C = C, B
    return C, B, A
print(SortDec3(31, 42, 4))