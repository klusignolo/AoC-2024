with open("input.txt", 'r') as input:
    parts = input.read().split("\n\n")
rules = parts[0].split('\n')
pages = parts[1].split('\n')
left_rules = {}
right_rules = {}
for rule in rules:
    vals = rule.split('|')
    left = vals[0]
    right = vals[1]
    if left not in left_rules.keys():
        left_rules[left] = [right]
    else:
        left_rules[left].append(right)
    if right not in right_rules.keys():
        right_rules[right] = [left]
    else:
        right_rules[right].append(left)

# right_rules: the key is the num and the vals are nums that should be to its left
invalid_pages = []
for page in pages:
    is_valid_page = True
    invalid_nums = []
    nums_visited = []
    for num in page.split(","):
        if num not in left_rules.keys(): left_rules[num] = []
        if num not in right_rules.keys(): right_rules[num] = []
        # Check if anything to the left of this num shouldn't have been there
        for num_rule in left_rules[num]:
            if num_rule in nums_visited:
                is_valid_page = False
                break
        nums_visited.append(num)
        # Check if current num is in the list of nums that shouldn't be to the right of previous nums
        if num in invalid_nums:
            is_valid_page = False
            break
        invalid_nums.extend(right_rules[num])
    if not is_valid_page: invalid_pages.append(page)
total = 0
for invalid_page in invalid_pages:
    numbers = invalid_page.split(',')
    mid_index = int((len(numbers) - 1) / 2)
    total += int(numbers[mid_index])
print(total)
