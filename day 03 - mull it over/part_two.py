import re

with open("input.txt", 'r') as input:
    pattern = r"mul\((\d{1,3},\d{1,3})\)"
    program = input.read()
    do_instructions = program.split("do()")
    sub_programs = [instruction.split("don't()")[0] for instruction in do_instructions]
    multipliers = []
    for instruction in sub_programs:
        multipliers.extend(re.findall(pattern, instruction))
result = 0
for multiplier in multipliers:
    vals = multiplier.split(",")
    result += int(vals[0]) * int(vals[1])
print(result)