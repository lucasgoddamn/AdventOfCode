import itertools

numbers = []
with open("nineinput") as f:
    for i in f.read().splitlines():
        numbers.append(int(i))

def solve1():
    for i in range(25, len(numbers)):
        current = numbers[i]
        for a, b in itertools.combinations(numbers[i-25:i], 2):
            if a + b == current:
                break
        else:
            return current

print(solve1())

def solve2():
    target = solve1()
    for a in range(len(numbers)):
        cum = 0
        for b in range(len(numbers) - a):
            cum += numbers[a+b]
            if b >= 1 and cum == target:
                x = numbers[a:a+b+1]
                return min(x) +max(x)
            elif cum > target:
                break

print(solve2())