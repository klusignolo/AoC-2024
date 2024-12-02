from collections import Counter
left_list = []
right_list = []
with open("input.txt", 'r') as input:
    for line in input.readlines():
        cols = line.split()
        left_list.append(int(cols[0]))
        right_list.append(int(cols[1]))
        
left_dict = Counter(left_list)
right_dict = Counter(right_list)
sim_total = 0
for number, left_count in left_dict.items():
    if number in right_dict.keys():
        right_count = right_dict[number]
        sim_score = number * right_count
        sim_total += sim_score * left_count
print(sim_total)