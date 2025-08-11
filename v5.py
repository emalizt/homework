price = float(input("Введите стоимость 1 кг конфет: "))
weight = 1.2
for i in range(1, 5):
    cost = price * weight
    weight += 0.2

    print(f"Стоимость: ", cost)
    print(weight)

# while weight <= 2.0:
#     cost = price * weight
#     weight += 0.2