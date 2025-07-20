def move_dir(y, x, directs):
    diry, dirx = directs
    dy = y + diry
    dx = x + dirx
    if dy < -5 or dy > 5 or dx < -5 or dx > 5:
        return y, x
    return dy, dx

def solution(dirs):
    direction_map = {
        "U": (1, 0),
        "D": (-1, 0),
        "R": (0, 1),
        "L": (0, -1)
    }

    y, x = 0, 0
    checked = set()

    for move in dirs:
        dy, dx = move_dir(y, x, direction_map[move])
        if (dy, dx) == (y, x):
            continue
        edge = tuple(sorted([(y, x), (dy, dx)]))
        checked.add(edge)
        y, x = dy, dx
    return len(checked)
