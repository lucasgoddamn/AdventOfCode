with open("fiveinput") as f:
    seats = f.readlines()

divseats = []
seatIDs = []
for i in seats:
    row = int(i[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(i[7:].replace('L', '0').replace('R', '1').replace('\n', ''), 2)
    divseats.append((row, col))

for i in divseats:
    seatIDs.append(i[0] * 8 + i[1])

seatIDs.sort(reverse=True)
print(max(seatIDs))
print(seatIDs)

x = set(range(min(seatIDs), max(seatIDs)+1)) - set(seatIDs)
print(x)
    