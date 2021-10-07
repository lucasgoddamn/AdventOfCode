with open("eightinput") as f:
    cmds = f.read().splitlines()

def solve():
    acc = 0
    cmd = 0
    seen = set()
    while cmd < len(cmds):
        if cmd in seen:
            break
        seen.add(cmd)

        a, b = cmds[cmd].split()
        if a == "acc":
            acc += int(b)
            cmd += 1
        elif a == "jmp":
            cmd += int(b)
        elif a == "nop":
            cmd += 1
    return acc

print(solve())


def simulate(flip):
    acc = 0
    cmd = 0
    seen = set()
    while cmd < len(cmds):
        if cmd in seen:
            return None
        seen.add(cmd)

        a, b = cmds[cmd].split()
        if cmd == flip:
            if a == "nop":
                a = "jmp"
            elif a == "jmp":
                a = "nop"
        if a == "acc":
            acc += int(b)
            cmd += 1
        elif a == "jmp":
            cmd += int(b)
        elif a == "nop":
            cmd += 1
    return acc


def solve2():
    for i in range(len(cmds)):
        if (out := simulate(i)) is not None:
            return out


print(solve2())
