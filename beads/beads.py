"""
ID: tejas.s2
LANG: PYTHON2
TASK: beads
"""
fin = open('beads.in', 'r')
fout = open('beads.out', 'w')
number_of_beads = int(fin.readline())
beads = str(fin.readline())
c1 = 0
c2 = 0
maximum = 0
for i in range(number_of_beads):
    before = beads[(i-1) % number_of_beads]
    after = beads[i % number_of_beads]
    if before != after:
        c1 = 0
        c2 = 0
        index = i - 1
        while beads[index] == before or beads[index] == 'w':
            sc = beads[index]
            c1 += 1
            if index == 0:
                index = number_of_beads - 1
            else:
                index -= 1
        index = i
        while beads[index % number_of_beads] == after or beads[index % number_of_beads] == 'w':
            c2 += 1
            if index == number_of_beads - 1:
                index = 0
            else:
                index += 1
        if maximum < (c1 + c2):
            maximum = c1 + c2
fout.write(str(maximum) + '\n')
fout.close()