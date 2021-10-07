from functools import reduce

with open("sixinput") as f:
    groups = f.read().split("\n\n")

x = 0
for i in groups:
    x += len(set(i.replace("\n", "" )))

print((x))

y = 0
for i in groups:
    y += len(reduce(set.intersection, map(set, i.split())))

print(y)