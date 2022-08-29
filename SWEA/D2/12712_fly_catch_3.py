
def plus_fly(y,x):
    cnt=arr[y][x]
    diry=[1,-1,0,0]
    dirx=[0,0,1,-1]
    for j in range(4):
        for i in range(1,M):
            dy=y+diry[j]*i
            dx=x+dirx[j]*i
            if dy<0 or dy>N-1 or dx<0 or dx>N-1:continue
            cnt+=arr[dy][dx]
    return cnt

def X(y,x):
    cnt=arr[y][x]
    diry=[-1,-1,1,1]
    dirx=[-1,1,1,-1]
    for j in range(4):
        for i in range(1,M):
            dy=y+diry[j]*i
            dx=x+dirx[j]*i
            if dy<0 or dy>N-1 or dx<0 or dx>N-1:continue
            cnt+=arr[dy][dx]
    return cnt

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    li=[]
    for y in range(N):
        for x in range(N):
            rat=plus_fly(y,x)
            li.append(rat)
            rat=X(y,x)
            li.append(rat)
    print(f'#{t+1} {max(li)}')