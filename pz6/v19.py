import random
c = []
i = 0
while i < 11:
    c.append(random.randint(0,100))
    i += 1
print(c)

def task_1(list, k , l):
    tot_sum = 0
    for i in range(1, (len(list) - 1)):
        if 1 < k and k < l:
            tot_sum += list[i]
    print(tot_sum)
k = 3
l = 8
task_1(c, k, l)


def task_2(list):
    print(len(set(list)))
list = [1, 2, 2, 3, 3, 4, 5,5, 6,6,6]

task_2(list)



