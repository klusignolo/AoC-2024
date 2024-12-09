with open("input.txt", 'r') as input:
    node_map = [[node for node in line] for line in input.read().split("\n")]

# Loop through map and make a dictionary. Key: node_name , Value: list of x,y coords
# Now loop through dictionary and use slope between coord a & coord b to get points c & d.
# c & d are antinode locations, provided that they do not extend beyond the scope of the map

map_width = len(node_map[0])
map_height = len(node_map)
node_dict = {}
for x in range(map_width):
    for y in range(map_height):
        node = node_map[y][x]
        if node == ".": continue
        if node in node_dict.keys():
            node_dict[node].append((x,y))
        else:
            node_dict[node] = [(x,y)]
antinode_locations = set()
for node, coord_list in node_dict.items():
    if len(coord_list) == 1: continue
    for i, a in enumerate(coord_list):
        if i == len(coord_list)-1: continue
        for j in range(len(coord_list)-i-1):
            b = coord_list[i+j+1]
            rise = b[1]-a[1]
            run = b[0]-a[0]
            slope = 0 if run == 0 else rise / run
            c,d = ([0,0],[0,0])
            if run >= 0:
                c[0] = a[0] - abs(run)
                d[0] = b[0] + abs(run)
            else:
                c[0] = a[0] + abs(run)
                d[0] = b[0] - abs(run)
            if rise >= 0:
                c[1] = a[1] - abs(rise)
                d[1] = b[1] + abs(rise)
            else:
                c[1] = a[1] + abs(rise)
                d[1] = b[1] - abs(rise)
                
            if c[0] >= 0 and c[1] >= 0 and c[0] < map_width and c[1] < map_height:
                key = f"{c[0]},{c[1]}"
                antinode_locations.add(key)
            if d[0] >= 0 and d[1] >= 0 and d[0] < map_width and d[1] < map_height:
                key = f"{d[0]},{d[1]}"
                antinode_locations.add(key)
print(len(antinode_locations))
# Curiously, it's the right answer for someone else. Too high: 396
