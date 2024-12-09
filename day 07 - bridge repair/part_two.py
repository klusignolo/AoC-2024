with open("input.txt", 'r') as input:
    equations = input.read().split("\n")
total = 0
def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))
for equation in equations:
    parts= equation.split(':')
    target_num = int(parts[0])
    operands = [int(x) for x in parts[1].strip().split()]
    options = 3 ** (len(operands)-1)
    for option in range(options):
        pattern = ternary(option)
        padding = "0" * (len(operands) - 1 - len(pattern))
        pattern = padding + pattern
        i = 0
        result = operands[i]
        for digit in pattern:
            if digit == "1":
                result *= operands[i+1]
            elif digit == "2":
                result = int(str(result) + str(operands[i+1]))
            else:
                result += operands[i+1]
            if result > target_num:
                break
            i += 1
            
        if result == target_num:
            total += target_num
            break
print(total)