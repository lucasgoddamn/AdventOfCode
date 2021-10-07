with open("twelveinput") as f:
    instr = f.read().splitlines()
    route = [(i[0], int(i[1:])) for i in instr]

pos = [0,0]
deg = 0

current_rotation = 0
rotation = {
    0: "E",
    90: "S",
    180: "W",
    270: "N"
}
for op, amount in route:
    orientation = rotation[current_rotation]
    if op == "F":
        op = orientation

    if op == "N":
        pos[1] += amount
    elif op == "S":
        pos[1] -= amount
    elif op == "E":
        pos[0] += amount
    elif op == "W":
        pos[0] -= amount
    elif op == "R":
        current_rotation = (current_rotation + amount) % 360
    elif op == "L":
        current_rotation = (current_rotation - amount) % 360
print(abs(pos[0]) + abs(pos[1]))
