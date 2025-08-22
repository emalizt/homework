import random
def task_1(a, d):
    list = []
    for i in range(10):
        list.append(a * d ** i)
#     print(list)
# task_1(2, 5)

c = []
i = 0
while i < 10:
    c.append(random.randint(0,100))
    i += 1
print(c)
def task_2(list):
    last_max = -1
    for i in range(1, len(list) - 1):
        if list[i] > list[i + 1] and list[i] > list[i - 1]:
            last_max = i
    print(last_max)
task_2(c)