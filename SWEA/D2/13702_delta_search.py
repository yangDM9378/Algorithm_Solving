def pattern(y,x):
    k=0
    for i in range(4):
        dy=y+diry[i]
        dx=x+dirx[i]
        if dy<0 or dy>N-1 or dx<0 or dx>N-1:
            continue
        k+=abs(arr[dy][dx]-arr[y][x])
    return k

for t in range(10):
    N=int(input())
    arr=[list(map(int, input().split())) for _ in range(N)]
    diry=[0,0,-1,1]
    dirx=[1,-1,0,0]
    a=0
    for y in range(N):
        for x in range(N):
            rat=pattern(y,x)
            a+=rat
    print(f'#{t+1} {a}')
