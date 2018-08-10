# https://old.reddit.com/r/dailyprogrammer/comments/8xzwl6/20180711_challenge_365_intermediate_sales/

input = """Revenue

            Johnver Vanston Danbree Vansey  Mundyke
Tea             190     140    1926     14      143
Coffee          325      19     293   1491      162
Water           682      14     852     56      659
Milk            829     140     609    120       87

Expenses

            Johnver Vanston Danbree Vansey  Mundyke
Tea             120      65     890     54      430
Coffee          300      10      23    802      235
Water            50     299    1290     12      145
Milk             67     254      89    129       76"""


lines = [line.split() for line in input.split("\n") if line]


_, *revenue = zip(*lines[2:len(lines)//2])
_, *expense = zip(*lines[2 + len(lines)//2:])

total = [sum(max(0,int(r) - int(e))*.062 for r,e in zip(*data)) for data in zip(revenue, expense)]
print_comm = [str(round(comm)).center(len(person)) for comm, person in zip(total,lines[1])]


print(f"            {' '.join(lines[1])}")
print(f"Comission  {' '.join(print_comm)}")
