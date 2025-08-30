import random
def task_1():
    list = []
    for i in range(1, 11):
        list.append(2 ** i)
    print("Степени двойки: ", list)
# task_1()


c = []
i = 0
while i < 10:
    c.append(random.randint(0,100))
    i += 1
print(c)


def task_2(list):
    list_index = []
    count = 0
    for i in range(1, len(list) - 1):
        if list[i] > list[i - 1]:
            list_index.append(i)
            count += 1
    print(list_index)
    print(count)
task_2(c)