import random
c = []
i = 0
while i < 11:
    c.append(random.randint(0,100))
    i += 1
print(c)

def task_1(list):
    em_list = []
    pol_spis = len(list) // 2
    for i in range(pol_spis, len(list)):
        em_list.append(list[i])
    for i in range(0, pol_spis):
        em_list.append(list[i])
    print(em_list)
task_1(c)
