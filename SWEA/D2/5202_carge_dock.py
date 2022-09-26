T=int(input())
for t in range(T):
    N=int(input())
    arr=[]
    for _ in range(N):
        k=list(map(int, input().split()))
        arr.append(k)
    arr.sort(key=lambda x:x[1])
    cnt=0
    temp=-1
    for i in arr:
        if i[0]>=temp:
            temp=i[1]
            cnt+=1
    print(f'#{t+1} {cnt}')

