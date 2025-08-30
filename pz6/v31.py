import random
c = []
i = 0
while i < 11:
    c.append(random.randint(0,100))
    i += 1
print(c)


def task_1(list):
    nechet = 0
    for i in range(0, len(list)):
        if list[i] % 2 == 1:
            nechet = list[i]
            break
    for i in range(0, len(list)):
        if list[i] % 2 == 1:
            list[i] += nechet

    return list
print(task_1(c))


