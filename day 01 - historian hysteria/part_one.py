left_list = []
right_list = []
with open("input.txt", 'r') as input:
    for line in input.readlines():
        cols = line.split()
        left_list.append(cols[0])
        right_list.append(cols[1])
    left_list.sort()
    right_list.sort()
diff = 0
for i, num in enumerate(left_list):
    diff += abs(int(num) - int(right_list[i]))
    
print(diff)