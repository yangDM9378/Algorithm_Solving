"""
입력 예시
5 6
101010
111111
000001
111111
111111
"""

from collections import deque
def bfs():
    q=deque()
    q.append((0,0,1))

    direct = [(0,1),(0,-1),(1,0),(-1,0)]
    while q:
        y,x,cnt = q.popleft()
        used[y][x]=cnt
        for i in range(4):
            dy = y + direct[i][0]
            dx = x + direct[i][1]
            if dy<0 or dx<0 or dy>N-1 or dx>M-1:continue
            if used[dy][dx]==0:
                q.append((dy,dx,cnt+1))

N,M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
used = [[0]*M for _ in range(N)]
bfs()
print(used[N-1][M-1])