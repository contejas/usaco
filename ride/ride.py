"""
ID: tejas.s2
LANG: PYTHON2
TASK: ride
"""
fin = open('ride.in', 'r')
fout = open('ride.out', 'w')
comet, group = str(fin.readline()[:-1]), str(fin.readline()[:-1])
let_to_num = dict(zip([char for char in 'abcdefghijklmnopqrstuvwxyz'.upper()], list(range(1,27))))
cometNum, groupNum = 1, 1
for char in comet:
    cometNum *= int(let_to_num[char])
for char in group:
    groupNum *= int(let_to_num[char])
cometNum, groupNum = cometNum % 47, groupNum % 47
output = 'GO\n' if cometNum == groupNum else 'STAY\n'
fout.write(output)
fout.close()
