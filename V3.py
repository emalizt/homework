price = float(input("Введите цену 1 кг конфет: "))
kg = 1
for i in range(1, 11):
    cost = i * price
    print("Стоимость конфет: ", cost)

# while kg <= 10:
#     cost = price * kg
#     kg += 1