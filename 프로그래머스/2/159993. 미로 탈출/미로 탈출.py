from collections import deque

def bfs(y,x,maps,cnt,search):
    q = deque()
    q.append([y,x,cnt])
    used = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    directs = [[0,1],[0,-1],[1,0],[-1,0]]
    used[y][x] = 1
    while q:
        y,x,cnt = q.popleft()
        for direct in directs:
            dy = y + direct[0]
            dx = x + direct[1]
            if dy < 0 or dx < 0 or dy > len(maps)-1 or dx > len(maps[0])-1: continue
            if used[dy][dx] != 0 or maps[dy][dx] =='X': continue
            if maps[dy][dx] == search:
                return [dy,dx,cnt+1]
            used[dy][dx] = 1
            q.append([dy,dx,cnt+1])
            


def solution(maps):
    answer = 0
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == 'S':
                S=[y,x]
    cnt=0
    L = bfs(S[0],S[1], maps, cnt, 'L')
    if L == None:
        return -1
    E = bfs(L[0],L[1], maps, L[2], 'E')
    if E == None:
        return -1
    return E[2]