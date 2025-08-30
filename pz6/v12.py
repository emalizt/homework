import random
c = []
i = 0
while i < 11:
    c.append(random.randint(0,100))
    i += 1
print(c)

def task_1(list):
    for i in range(len(list) - 1, - 1, -2):
        print(list[i], end=" ")
# task_1(c)

def task_2(list):
    sum_max = -1
    index_1 = -1
    index_2 = -1
    for i in range(0, len(list) - 2):
        if list[i] + list[i + 1] > sum_max:
            sum_max = list[i] + list[i + 1]
            index_1 = i
            index_2 = i + 1
    print(sum_max)
    print(index_1, index_2)
task_2(c)
