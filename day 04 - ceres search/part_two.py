XMAS_COUNT = 0

def is_x_mas(pos):
    y,x = pos
    up_left = rows[y-1][x-1] if y > 0 and x > 0 else None
    up_right = rows[y-1][x+1] if y > 0 and x < width-1 else None
    down_left = rows[y+1][x-1] if y < width-1 and x > 0  else None
    down_right = rows[y+1][x+1] if y < width-1 and x < width-1 else None

    if not up_left or not up_right or not down_left or not down_right:
        return False
    left_diag_is_mas = (up_left == "M" and down_right == "S") or (up_left == "S" and down_right == "M")
    right_diag_is_mas = (up_right == "M" and down_left == "S") or (up_right == "S" and down_left == "M")
    return left_diag_is_mas and right_diag_is_mas

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
            if char != "A": continue
            if is_x_mas(pos=(y, x)):
                XMAS_COUNT += 1
print(XMAS_COUNT)