from collections import deque
def bfs(endy, endx):
    global arr
    q=deque()
    q.append([endy,endx])
    arr[endy][endx] = 2
    while q:
        y,x=q.popleft()
        for direct in [(0,-1),(0,1),(1,0),(-1,0)]:
            dy = y+direct[0]
            dx = x+direct[1]
            if dy<0 or dy>n-1 or dx<0 or dx>m-1:continue
            if arr[dy][dx]==1:
                arr[dy][dx] = arr[y][x]+1
                q.append([dy,dx])

n,m=map(int, input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if arr[i][j]==2:
            endy = i
            endx = j
            break
bfs(endy, endx)
for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            print(0, end=' ')
        elif arr[i][j]==1:
            print(-1, end=' ')
        else:
            print(arr[i][j]-2, end=' ')
    print('')

