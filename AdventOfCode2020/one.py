numbers = []
with open("oneinput") as f:
    numbers = list(map(int, f.readlines()))

for i in numbers:
    x = 2020 - i
    for j in numbers:
        for k in numbers:
            if k+j == x:
                print(i*j*k)


#print(oneinput)
