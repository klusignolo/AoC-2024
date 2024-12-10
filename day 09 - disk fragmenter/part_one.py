with open("input.txt", 'r') as input:
    disk_map = [int(char) for char in input.read().replace('\n','')]
## 00...111...2...333.44.5555.6666.777.888899

# index count is the length of the line % 2
# start at the end and the beginning, fill spaces as you go
# right and left pointers
# right pointer moves when divvied out the nums
# right pointer can skip every other index because of free space
# left pointer moves along and creates the checksum, putting stuff from right pointer into spaces
left_pointer = 0
right_pointer = len(disk_map)-1
file_blocks = []
while left_pointer <= right_pointer:
    # Start looping left pointer to grab
    while left_pointer % 2 == 0:
        if disk_map[left_pointer] == 0:
            # Move left pointer when finished
            left_pointer += 1
            continue
        idx = int(left_pointer / 2)
        file_blocks.append(idx)
        disk_map[left_pointer] -= 1
    if disk_map[right_pointer] == 0:
        # Move right pointer when finished
        right_pointer -= 2
        continue
    elif disk_map[left_pointer] == 0:
        left_pointer += 1
        continue
    else:
        idx = int(right_pointer / 2)
        file_blocks.append(idx)
        disk_map[left_pointer] -= 1
        disk_map[right_pointer] -= 1
checksum = 0
for i, idx in enumerate(file_blocks):
    checksum += i * idx
print(checksum)
