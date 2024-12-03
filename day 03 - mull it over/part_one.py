import re

with open("input.txt", 'r') as input:
    pattern = r"mul\((\d{1,3},\d{1,3})\)"
    program = input.read()
    multipliers = re.findall(pattern, program)
result = 0
for multiplier in multipliers:
    vals = multiplier.split(",")
    result += int(vals[0]) * int(vals[1])
print(result)