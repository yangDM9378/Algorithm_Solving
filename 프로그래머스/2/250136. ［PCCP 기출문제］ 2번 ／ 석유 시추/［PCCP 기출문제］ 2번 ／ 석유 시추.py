from collections import deque

def depth_oil(y, x, land, used, check_oil):
    directs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    q = deque()
    q.append((y, x))
    used[y][x] = 1
    oil=1
    min_x, max_x = x,x
    while q:
        y, x = q.popleft()
        for direct in directs:
            dy = y + direct[0]
            dx = x + direct[1]
            if dy < 0 or dx < 0 or dy > len(land) - 1 or dx > len(land[0]) - 1:continue
            if used[dy][dx] == 0 and land[dy][dx] == 1:
                min_x=min(min_x,dx)
                max_x=max(max_x,dx)
                used[dy][dx] = 1
                oil += 1
                q.append((dy, dx))
    for idx in range(min_x, max_x+1):
        check_oil[idx]+=oil
        

def solution(land):
    used = [[0]*len(land[0]) for _ in range(len(land))]
    check_oil = [0] * len(land[0])
    for y in range(len(land)):
        for x in range(len(land[0])):
            if land[y][x] == 1 and used[y][x] == 0:
                depth_oil(y, x, land, used, check_oil)
                
    return max(check_oil)