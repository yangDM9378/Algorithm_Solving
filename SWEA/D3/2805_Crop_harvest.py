def a(N):
    z=[[0]*N for _ in range(N)]
    for i in range(int(N//2)+1):
        for j in range(int(N//2)-i):
            z[i][j]=1

    for i in range(int(N//2)+1):
        for j in range(int(N//2)-i):
            z[-i-1][-j-1]=1

    for i in range(int(N//2)+1):
        for j in range(int(N//2)-i):
            z[i][-j-1]=1

    for i in range(int(N//2)+1):
        for j in range(int(N//2)-i):
            z[-i-1][j]=1
    return z



T=int(input())
for t in range(1,T+1):
    N=int(input())
    arr=[list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j]=int(arr[i][j])
    z=a(N)
    result=0
    for i in range(N):
        for j in range(N):
            if z[i][j]==0:
                result+=arr[i][j]
    print(f'#{t} {result}')
