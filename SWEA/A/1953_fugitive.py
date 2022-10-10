import sys
sys.stdin = open("fugitive.txt", "r")
def dusruf(y,x,dy,dx,i):
    if arr[dy][dx]==1:
        return True
    elif arr[dy][dx]==2:
        if i in [0,2]:
            return True
    elif arr[dy][dx]==3:
        if i in [1,3]:
            return True
    elif arr[dy][dx]==4:
        if i in [2,3]:
            return True
    elif arr[dy][dx]==5:
        if i in [0,3]:
            return True
    elif arr[dy][dx]==6:
        if i in [0,1]:
            return True
    elif arr[dy][dx]==7:
        if i in [1,2]:
            return True
    return False

def dlehd(y,x,i):
    if arr[y][x]==1:
        return True
    elif arr[y][x]==2:
        if i in [0,2]:
            return True
    elif arr[y][x]==3:
        if i in [1,3]:
            return True
    elif arr[y][x]==4:
        if i in [0,1]:
            return True
    elif arr[y][x]==5:
        if i in [1,2]:
            return True
    elif arr[y][x]==6:
        if i in [2,3]:
            return True
    elif arr[y][x]==7:
        if i in [0,3]:
            return True
    return False


def bfs(y,x,L):
    global used
    q=deque()
    q.append((y,x,1))
    while q:
        node=q.popleft()
        nowy,nowx,level=node[0],node[1],node[2]
        if level>L:continue
        used[nowy][nowx]=1
        direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        # 이동
        for i in range(4):
            if dlehd(nowy,nowx,i):
                dy=nowy+direct[i][0]
                dx=nowx+direct[i][1]
                if dy < 0 or dy > N - 1 or dx < 0 or dx> M - 1: continue
                if used[dy][dx] == 1: continue
                # 연결
                if dusruf(nowy,nowx,dy,dx,i):
                    q.append((dy,dx,level+1))

from collections import deque
T=int(input())
for t in range(T):
    N,M,y,x,L=map(int,input().split())
    arr=[list(map(int, input().split())) for _ in range(N)]

    used=[[0]*M for _ in range(N)]
    bfs(y,x,L)
    cnt=0
    for i in range(N):
        for j in range(M):
            if used[i][j]==1:
                cnt+=1
    print(f'#{t+1} {cnt}')