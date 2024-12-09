with open("input.txt", 'r') as input:
    equations = input.read().split("\n")
total = 0
for equation in equations:
    parts= equation.split(':')
    target_num = int(parts[0])
    operands = [int(x) for x in parts[1].strip().split()]
    options = int("1" * (len(operands)-1), 2)
    for option in range(options+1):
        pattern = "{0:b}".format(option)
        padding = "0" * (len(operands) - 1 - len(pattern))
        pattern = padding + pattern
        i = 0
        result = operands[i]
        for digit in pattern:
            if digit == "1":
                result *= operands[i+1]
            else:
                result += operands[i+1]
            if result > target_num:
                break
            i += 1
            
        if result == target_num:
            total += target_num
            break
print(total)
#1038838603811 too high
#1038838357795