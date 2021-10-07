from collections import Counter

with open("teninput") as f:
    numbers = sorted(list(map(int, f.read().splitlines())))

def solve1():
    prev = 0
    counter = Counter()
    for x in numbers:
        d = x - prev
        counter[d] += 1
        prev = x
    counter[3] += 1
    return counter[1] * counter[3]

print(solve1())

dp = {}
def count(idx, joltage):
    if idx == len(numbers):
        return joltage == numbers[-1]
    if numbers[idx] - joltage > 3:
        return 0

    if (idx, joltage) not in dp:
        dp[(idx, joltage)] = count(idx + 1, joltage) + count(idx + 1, numbers[idx])
    return dp[(idx, joltage)]

def solve2():
    dp.clear()
    return count(0, 0)

print(solve2())


