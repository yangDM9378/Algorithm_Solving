"""
입력예시
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

입력예시
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

입력예시
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
"""
from collections import deque
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
used = [[0]*m for _ in range(n)]
direct = [(-1,0),(0,1),(1,0),(0,-1)]
result = 0
def virus(y,x):
    for move in direct:
        dy = y+move[0]
        dx = x+move[1]
        if dy<0 or dx<0 or dy>n-1 or dx>m-1:continue
        if used[dy][dx]==0:
            used[dy][dx]=2
            virus(dy,dx)

def safe_area():
    area_cnt =0
    for i in range(n):
        for j in range(m):
            if used[i][j]==0:
                area_cnt+=1
    return area_cnt

def dfs(cnt):
    global result
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                used[i][j] = arr[i][j]

        for i in range(n):
            for j in range(m):
                if used[i][j]==2:
                    virus(i,j)
        result = max(result, safe_area())
        return

    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                arr[i][j]=1
                cnt+=1
                dfs(cnt)
                arr[i][j]=0
                cnt -=1
dfs(0)
print(result)