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
            map[pos_y][pos_x] = dir
            break
next_dir = {"n":"e","e":"s","s":"w","w":"n"}


intersect_set = set()
starting_pos_key = f"{pos_x},{pos_y}"

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

    # Move forward
    did_hit_obstacle = next_space == "#"
    if did_hit_obstacle:
            dir = next_dir[dir]
            pos_x,pos_y = original_pos
    else:
        map[pos_y][pos_x] += dir

    
    # Check all to the right
    explore_dir = next_dir[dir]
    exploring = not did_hit_obstacle
    explore_x,explore_y = original_pos # use 
    explored_spaces = set()
    found_explore_loop = False
    explore_key = f"{pos_x},{pos_y}"
    map[pos_y][pos_x] += "?"
    while exploring:
        original_explore_pos = (explore_y,explore_x)
        match explore_dir:
            case "n":
                explore_y -= 1
            case "s":
                explore_y += 1
            case "e":
                explore_x += 1
            case "w":
                explore_x -= 1
        next_explore_space = map[explore_y][explore_x]
        set_key = f"{explore_x}{explore_y}{explore_dir}"
        if set_key in explored_spaces:
            found_explore_loop = True
            exploring = False
            continue
        else:
            explored_spaces.add(set_key)
        if explore_dir in next_explore_space:
            found_explore_loop = True
            exploring = False
            continue
        out_of_range = explore_x <= 0 or explore_y <= 0 or explore_x >= map_width-1 or explore_y >= map_height-1
        if out_of_range:
            exploring = False
            continue
        if "#" in next_explore_space or "?" in next_explore_space:
            explore_dir = next_dir[explore_dir]
            explore_y,explore_x = original_explore_pos
    if found_explore_loop and explore_key != starting_pos_key:
        intersect_set.add(explore_key)
    map[pos_y][pos_x] = map[pos_y][pos_x].replace("?","")

print(len(intersect_set))