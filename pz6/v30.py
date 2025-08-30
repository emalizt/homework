import random
c = []
i = 0
while i < 11:
    c.append(random.randint(0,100))
    i += 1
print(c)

def task_1(list):
    chet = 0
    flag = True
    for i in range(0, len(list)):
        if list[i] % 2 == 0 and flag:
            chet = list[i]
            flag = False
    for i in range(0, len(list)):
        if list[i] % 2 == 0:
            list[i] += chet
    return list
# print(task_1(c))
list = [3, 5, 7]
for i in range(0, len(list)):
    print(list[i])

def task_2(list):
    list_B = []
    summ = 0
    for num  in list:
        summ = summ + num
        list_B.append(summ)
    print(list_B)
# task_2([1, 2, 3, 4, 5])

def task_3(list, k):
    list_a = []
    for i in range(0, k):
        list_a.append(0)
    for i in range(0, len(list) - k):
        list_a.append(list[i])
    print(list_a)

# task_3(c, 5)

def task3_1(list, k):
    list_a = []
    for i in range(0, len(list) - k):
        list_a.append(list[i])
    for i in range(0, k):
        list_a.append(0)
    print(list_a)

# task3_1(c, 3)