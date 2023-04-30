def dfs(y,x, color):
    global used
    global result_cnt
    used[y][x] = 1
    diry = [0,0,-1,1]
    dirx = [1,-1,0,0]
    for i in range(4):
        dy=y+diry[i]
        dx=x+dirx[i]
        if dy<0 or dy>n-1 or dx<0 or dx>n-1:continue
        if used[dy][dx]==1 or origin_image[dy][dx]!=color: continue
        used[dy][dx]=1
        dfs(dy,dx,color)



n=int(input())
used = [[0]*n for _ in range(n)]
origin_image = [list(input()) for _ in range(n)]
result_cnt = 0

# origin 영역 판단 하는 dfs
for y in range(n):
    for x in range(n):
        if used[y][x] == 1:continue
        dfs(y,x,origin_image[y][x])
        result_cnt+=1
print(result_cnt, end=' ')

for y in range(n):
    for x in range(n):
        if origin_image[y][x] == 'G':
            origin_image[y][x] = 'R'

used = [[0]*n for _ in range(n)]
result_cnt = 0

for y in range(n):
    for x in range(n):
        if used[y][x] == 1:continue
        dfs(y,x,origin_image[y][x])
        result_cnt+=1
print(result_cnt)
