from collections import deque

def bfs(tomato_init):
    global tomato_arr
    q=deque()
    for init in tomato_init:
        q.append(init)
    diry=[0,0,-1,1]
    dirx=[-1,1,0,0]
    while q:
        y,x,value = q.popleft()
        for i in range(4):
            dy=y+diry[i]
            dx=x+dirx[i]
            if dy<0 or dy>m-1 or dx<0 or dx>n-1: continue
            if tomato_arr[dy][dx] != 0: continue
            toma_cnt = value+1
            tomato_arr[dy][dx]=toma_cnt
            q.append([dy,dx,toma_cnt])


n,m = map(int, input().split())
tomato_arr=[list(map(int, input().split())) for _ in range(m)]
tomato_init=[]
# 초기토마토위치들
for y in range(m):
    for x in range(n):
        if tomato_arr[y][x] == 1:
            tomato_init.append([y,x,1])

bfs(tomato_init)
def result_cnt(tomato_arr):
    max_cnt = 0
    for i in range(m):
        for j in range(n):
            if tomato_arr[i][j] == 0:
                return -1
            if max_cnt < tomato_arr[i][j]:
                max_cnt = tomato_arr[i][j]
    return max_cnt-1
print(result_cnt(tomato_arr))