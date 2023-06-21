"""
입력 에시
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""

N,M = map(int, input().split())
y,x,see = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
see_arr = [[-1,0],[0,1],[1,0],[0,-1]]

cnt=0
result=1
while True:
    arr[y][x]=1
    if cnt == 4:
        break
    see = (see+1)%4
    cnt = cnt+1
    dy=y+see_arr[see][0]
    dx=x+see_arr[see][1]
    if 0<=dy<M and 0<=dx<N:
        if arr[dy][dx] == 0:
            y=dy
            x=dx
            result+=1
            cnt=0
print(result)