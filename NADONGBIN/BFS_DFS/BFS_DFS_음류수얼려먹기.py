"""
입력 예시
4 5
00110
00011
11111
00000
"""

from collections import deque

def bfs(y,x):
    q=deque()
    q.append((y,x))
    direct=[(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        y, x = q.popleft()
        used[y][x]=1
        for i in range(4):
            dy=y+direct[i][0]
            dx=x+direct[i][1]
            if 0<=dy<len(arr) and 0<=dx<len(arr[0]):
                if arr[dy][dx]=='0' and used[dy][dx]==0:
                    q.append((dy,dx))

N,M = map(int, input().split())
arr=[list(input()) for _ in range(N)]
used=[[0]*M for _ in range(N)]
cnt=0
for y in range(N):
    for x in range(M):
        if arr[y][x]=='0' and used[y][x]==0:
            bfs(y,x)
            cnt+=1
print(cnt)