import re
lines = []

with open("twoinput") as f:
    lines = f.readlines()
def xor(x, y):
    return bool((x and not y) or (not x and y))

valid = 0
valid2 = 0
pattern = '([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)'
for i in lines:
    match = re.search(pattern, i)
    min_amount = int(match.group(1))
    max_amount = int(match.group(2))
    char = match.group(3)
    password = match.group(4)
    count = password.count(char)
    if count >= min_amount and count <= max_amount:
        valid += 1
    if xor(password[min_amount -1] == char, password[max_amount -1] == char):
        valid2 += 1

print(valid)
print(valid2)

