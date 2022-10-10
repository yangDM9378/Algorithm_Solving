import sys
sys.stdin = open("home_crime_prevention_service.txt", "r")
from collections import deque
def service_price(k):
    global max_house
    for y in range(N):
        for x in range(N):
            house=bfs(k,y,x)
            if house*M-sp>=0:
                max_house=max(max_house,house)

def bfs(k,y,x):
    li = [[0]*N for _ in range(N)]
    li[y][x]=1
    cnt=0
    q=deque()
    q.append((1, y, x))
    while q:
        nowk,nowy,nowx=q.popleft()
        if arr[nowy][nowx]==1:
            cnt+=1
        diry=[-1,1,0,0]
        dirx=[0,0,-1,1]
        for i in range(4):
            dy=diry[i]+nowy
            dx=dirx[i]+nowx
            if dy<0 or dy>N-1 or dx<0 or dx>N-1:continue
            if li[dy][dx]==1:continue
            li[dy][dx]=1
            if nowk<k:
                q.append((nowk+1,dy,dx))
    return cnt

T=int(input())
for t in range(T):
    N, M=map(int, input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    max_house=-21e8
    for k in range(1,N+2):
        sp=k*k+(k-1)*(k-1)
        service_price(k)
    print(f'#{t+1} {max_house}')
