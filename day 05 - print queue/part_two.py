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

# Do solution from part one, but stash the invalid pages now.
invalid_pages = []
for page in pages:
    is_valid_page = True
    invalid_nums = []
    nums_visited = []
    for num in page.split(","):
        if num not in left_rules.keys(): left_rules[num] = []
        if num not in right_rules.keys(): right_rules[num] = []
        for num_rule in left_rules[num]:
            if num_rule in nums_visited:
                is_valid_page = False
                break
        nums_visited.append(num)
        if num in invalid_nums:
            is_valid_page = False
            break
        invalid_nums.extend(right_rules[num])
    if not is_valid_page: invalid_pages.append(page)

# Loop through the invalid pages and fix them all.
# The horribly inefficient "fix" algorithm basically does the following:
# Loop through a page's numbers. For each number, check all numbers to the left and right.
# If any number to the left or right is found to create an invalid page, swap places with the current number.
# Start over again with the same page and keep swapping/restarting until the page comes out clean.
valid_pages = []
for page in invalid_pages:
    nums = page.split(",")
    i = 0
    while i < len(nums):
        this_num = nums[i]
        for j, that_num in enumerate(nums):
            if i == j: continue
            elif i < j:
                l_rules = left_rules.get(this_num)
                if l_rules and that_num in l_rules:
                    nums[i] = that_num
                    nums[j] = this_num
                    i = 0
                    break
                r_rules = right_rules.get(that_num)
                if r_rules and this_num in r_rules:
                    nums[i] = that_num
                    nums[j] = this_num
                    i = 0
                    break
            elif i > j:
                l_rules = left_rules.get(that_num)
                if l_rules and this_num in l_rules:
                    nums[i] = that_num
                    nums[j] = this_num
                    i = 0
                    break
                r_rules = right_rules.get(this_num)
                if r_rules and that_num in r_rules:
                    nums[i] = that_num
                    nums[j] = this_num
                    i = 0
                    break
            #----
        i += 1
    valid_pages.append(",".join(nums))

total = 0
for valid_page in valid_pages:
    numbers = valid_page.split(',')
    mid_index = int((len(numbers) - 1) / 2)
    total += int(numbers[mid_index])
print(total)
