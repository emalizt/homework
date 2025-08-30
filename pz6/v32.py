import random
c = []
i = 0
while i < 11:
    c.append(random.randint(0,100))
    i += 1
print(c)

def task_1(list):
    min_el = 0
    max_el = 0
    znach_max = 0
    znach_min = list[0]
    for i in range(0, len(list)):
        if list[i] <= znach_min:
            min_el = i
            znach_min = list[i]
        if list[i] >= znach_max:
            max_el = i
            znach_max = list[i]
    list[min_el], list[max_el] = list[max_el], list[min_el]
    print(znach_max)
    print(znach_min)
    print(min_el)
    print(max_el)
    return list
# print(task_1(c))

def task_2(list):
    list_B = []
    summ = 0
    for num in list:
        summ = summ + num
        list_B.append(summ)
    print(list_B)
# task_2(c)
def task_3(list, k):
    list_a = []
    for i in range(0, len(list) - k):
        list_a.append(list[i])
    for i in range(0, k):
        list_a.append(0)
    print(list_a)
task_3(c, 4)






# def task_3(list:)
#     for i in range(0, len(list)):
#