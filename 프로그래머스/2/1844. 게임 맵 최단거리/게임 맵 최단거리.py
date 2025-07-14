from collections import deque
def solution(maps):
    h = len(maps)
    w = len(maps[0])
    used = [[0]*w for _ in range(h)]
    q = deque()
    q.append((0,0,1))
    used[0][0]=1
    while q:
        y,x,cnt = q.popleft()
        if y == (h-1) and x == (w-1):
            return cnt
        for direct in [[0,1],[0,-1],[1,0],[-1,0]]:
            diry, dirx = direct[0], direct[1]
            dy = y+diry
            dx = x+dirx
            if dy<0 or dy>h-1 or dx<0 or dx>w-1:continue
            if used[dy][dx] == 0 and maps[dy][dx] == 1:
                used[dy][dx] = 1
                q.append((dy,dx,cnt+1))
    return -1