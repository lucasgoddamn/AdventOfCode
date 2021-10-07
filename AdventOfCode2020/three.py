with open("threeinput") as f:
    biome = [line.replace('\n', "") for line in f]

counter = 0
pos_x = 0
right = 1
down = 2

for pos_y in range(0, len(biome), down):
    if biome[pos_y][pos_x] == "#":
        counter += 1
    pos_x = (pos_x + right) % len(biome[0])

print(counter)

print(77*280*74*78*counter)