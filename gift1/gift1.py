"""
ID: tejas.s2
LANG: PYTHON2
TASK: gift1
"""
fin = open('gift1.in', 'r')
fout = open('gift1.out', 'w')
NP = int(fin.readline())
people = {}
order = []
for i in range(NP):
    pers = str(fin.readline()[:-1])
    people[pers] = 0
    order.append(pers)
for j in range(NP):
    person = str(fin.readline()[:-1])
    money_iter = list(fin.readline().split())
    if int(money_iter[0]) == 0:
        for k in range(int(money_iter[1])):
            fin.readline()
    else:
        people[person] += (int(money_iter[0]) % int(money_iter[1]) - int(money_iter[0]))
        for k in range(int(money_iter[1])):
            people[str(fin.readline()[:-1])] += (int(money_iter[0]) / int(money_iter[1]))
for person in order:
    fout.write(str(person) + " " + str(people[person]) + '\n')
fout.close()