XMAS_COUNT = 0

def look_for_next_char(curr_char, curr_pos, dir="any"):
    if curr_char == "S":
        global XMAS_COUNT
        XMAS_COUNT += 1
        return
    
    next_char = ""
    y, x = curr_pos
    if curr_char == "X":
        next_char = "M"
    elif curr_char == "M":
        next_char = "A"
    else:
        next_char = "S"
        
    up = rows[y-1][x] if y > 0 and dir in ("any", "n") else None
    up_left = rows[y-1][x-1] if y > 0 and x > 0 and dir in ("any", "nw") else None
    up_right = rows[y-1][x+1] if y > 0 and x < width-1 and dir in ("any", "ne") else None
    down = rows[y+1][x] if y < width-1 and dir in ("any", "s") else None
    down_left = rows[y+1][x-1] if y < width-1 and x > 0 and dir in ("any", "sw") else None
    down_right = rows[y+1][x+1] if y < width-1 and x < width-1 and dir in ("any", "se") else None
    left = rows[y][x-1] if x > 0 and dir in ("any", "w") else None
    right = rows[y][x+1] if x < width-1 and dir in ("any", "e") else None

    if up and up == next_char:
        look_for_next_char(up, (y-1, x), dir="n")
    if down and down == next_char:
        look_for_next_char(down, (y+1, x), dir="s")
    if left and left == next_char:
        look_for_next_char(left, (y, x-1), dir="w")
    if right and right == next_char:
        look_for_next_char(right, (y, x+1), dir="e")
    if up_left and up_left == next_char:
        look_for_next_char(up_left, (y-1, x-1), dir="nw")
    if up_right and up_right == next_char:
        look_for_next_char(up_right, (y-1, x+1), dir="ne")
    if down_left and down_left == next_char:
        look_for_next_char(down_left, (y+1, x-1), dir="sw")
    if down_right and down_right == next_char:
        look_for_next_char(down_right, (y+1, x+1), dir="se")

with open("input.txt", 'r') as input:
    rows = [[char for char in line] for line in input.read().split("\n")]
    width = len(rows)
    cols = [[] for _ in range(width)]
    for row in rows:
        for i, char in enumerate(row):
            cols[i].append(char)
    for y in range(width):
        for x in range(width):
            char = rows[y][x]
            if char != "X": continue
            else: look_for_next_char(char, (y, x))
print(XMAS_COUNT)