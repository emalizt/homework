import random
from turtledemo.penrose import start


def task_1():
    list = []
    for i in range(10):
        list.append(2 * i + 1)

    print(list)
# task_1()

def task_2(list):
    index = []
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            index.append(i)
    print("индекс", index)
    print("Кол-во индекса", len(index))

c = []
i = 0
while i < 10:
    c.append(random.randint(0,100))
    i += 1
print(c)
# task_2(c)

def task_3(a, k, l):
    start = k + 1
    end = l - 1
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1
    print(a)
task_3(c, 0, 9)
