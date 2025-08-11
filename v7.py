A = int(input("Введите A: "))
B = int(input("Введите B: "))
prod = 1
for i in range(A, B + 1):
    prod *= i
print("Произведение всех чисел от", A, "до", B, "равно", prod)
