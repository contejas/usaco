"""
ID: tejas.s2
LANG: PYTHON2
TASK: friday
"""
fin = open('friday.in', 'r')
fout = open('friday.out', 'w')
N = int(fin.readline())
output = {1:0,2:0,3:0,4:0,5:0,6:0,7:0}
months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
day_of_the_week = 3  # Monday is 3, Tuesday is 4, Sunday is 2
month = 1
day = 1
year = 1900
leap = False
end_year = (1900 + N) - 1
while year != end_year or day != 31 or month != 12:
    day += 1
    if day == months[month] + 1:
        month += 1
        day = 1
        if month == 13:
            month = 1
            year += 1
    if year % 4 == 0:
        if str(year)[2:4] == "00":
            if year % 400 == 0:
                months[2] = 29
        else:
            months[2] = 29
    else:
        months[2] = 28
    day_of_the_week += 1
    if day_of_the_week == 8:
        day_of_the_week = 1
    if day == 13:
        output[day_of_the_week] += 1
for key in output:
    if key == 7:
        fout.write(str(output[key]))
    else:
        fout.write(str(output[key]) + " ")