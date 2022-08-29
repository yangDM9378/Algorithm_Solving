def a(y,x):
    ssum=0
    for i in range(M):
        for j in range(M):
            ssum+=arr[y+i][x+j]
    return ssum

T=int(input())
for t in range(T):
    N,M=map(int, input().split())
    arr=[list(map(int, input().split())) for _ in range(N)]
    Maxssum=0
    for y in range(N-M+1):
        for x in range(N-M+1):
            rat=a(y,x)
            if Maxssum<rat:
                Maxssum=rat
    print(f'#{t+1} {Maxssum}')