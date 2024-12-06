with open("input.txt", 'r') as input:
    map = [[item for item in line] for line in input.read().split("\n")]
pos_x = None
pos_y = None
dir = "n"
has_escaped = False
map_width = len(map[0])
map_height = len(map)
# get starting pos
for y_index, row in enumerate(map):
    if pos_y or pos_x: break
    for x_index, col in enumerate(row):
        if col == "^":
            pos_x = x_index
            pos_y = y_index
            map[pos_y][pos_x] = "X"
            break
next_dir = {"n":"e","e":"s","s":"w","w":"n"}
while not has_escaped:
    original_pos = (pos_x,pos_y)
    match dir:
        case "n":
            pos_y -= 1
        case "s":
            pos_y += 1
        case "e":
            pos_x += 1
        case "w":
            pos_x -= 1
    if pos_x < 0 or pos_y < 0 or pos_x >= map_width or pos_y >= map_height:
        has_escaped = True
        continue
    next_space = map[pos_y][pos_x]
    if next_space == "#":
            dir = next_dir[dir]
            pos_x,pos_y = original_pos
    else:
        map[pos_y][pos_x] = "X"
x_count = 0
for row in map:
    for col in row:
        x_count += 1 if col == "X" else 0
print(x_count)