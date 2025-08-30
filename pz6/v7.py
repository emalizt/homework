import random

def task_1(list):
    count = 0
    for i in range(0, len(list) - 1):
        if list[i] % 2 == 1:
            print(list[i], end=" ")

            count += 1
    print()
    print(count)





c = []
i = 0
while i < 10:
    c.append(random.randint(0,100))
    i += 1
print(c)

# task_1(c)

def task_2(list):
    min_loc_max = list[1]
    for i in range(1, len(list) - 2):
        if list[i] > list[i - 1] and list[i] > list[i + 1] and list[i] < min_loc_max:
            min_loc_max = list[i]

    return min_loc_max
print(task_2(c))