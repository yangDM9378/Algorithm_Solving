T=int(input())
for k in range(T):
    N=int(input())
    arr=list(map(int, input().split()))
    li=[]
    for i in range(N):
        cnt=0
        for j in range(i+1,N):
            if arr[i]<=arr[j]:
                cnt+=1
        li.append(N -cnt -1 -i)
    print(f'#{k+1} {max(li)}')