with open("input.txt", 'r') as input:
    node_map = [[node for node in line] for line in input.read().split("\n")]

# Same approach as part_one, but continue expanding the "c" and "d" nodes outward until out of bounds.

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
            antinode_locations.add(f"{a[0]},{a[1]}")
            antinode_locations.add(f"{b[0]},{b[1]}")
            rise = b[1]-a[1]
            run = b[0]-a[0]
            slope = 0 if run == 0 else rise / run
            c,d = ([0,0],[0,0])

            c_is_in_bounds = True
            start = [a[0],a[1]]
            while c_is_in_bounds:
                if run >= 0:
                    c[0] = start[0] - abs(run)
                else:
                    c[0] = start[0] + abs(run)
                if rise >= 0:
                    c[1] = start[1] - abs(rise)
                else:
                    c[1] = start[1] + abs(rise)
                    
                if c[0] >= 0 and c[1] >= 0 and c[0] < map_width and c[1] < map_height:
                    key = f"{c[0]},{c[1]}"
                    antinode_locations.add(key)
                    start[0]=c[0]
                    start[1]=c[1]
                else:
                    c_is_in_bounds = False

            d_is_in_bounds = True
            start = [b[0],b[1]]
            while d_is_in_bounds:
                if run >= 0:
                    d[0] = start[0] + abs(run)
                else:
                    d[0] = start[0] - abs(run)
                if rise >= 0:
                    d[1] = start[1] + abs(rise)
                else:
                    d[1] = start[1] - abs(rise)
                if d[0] >= 0 and d[1] >= 0 and d[0] < map_width and d[1] < map_height:
                    key = f"{d[0]},{d[1]}"
                    antinode_locations.add(key)
                    start[0]=d[0]
                    start[1]=d[1]
                else:
                    d_is_in_bounds = False
print(len(antinode_locations))
