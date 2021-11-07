import random
n = [random.randint (-999, 999) for i in range (10)]
Spisok = len(n)
print("Список", str(n))

nechetnye = []
for i in range(Spisok):
    if n[i] % 2 != 0:
        nechetnye.append(n[i])

from functools import reduce
items = list(nechetnye)
all_max = reduce(lambda a,b: a if (a > b) else b, items)

print (all_max)

from functools import reduce
items = list(n)
all_minmod = reduce(lambda a,b: a if (abs(a) < abs(b)) else b, items)

print (all_minmod)
