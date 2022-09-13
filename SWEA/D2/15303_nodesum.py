def preorder(now):
    if now>len(arr)-1:
        return
    preorder(now*2)
    preorder(now*2+1)
    arr[now//2]+=arr[now]
T=int(input())
for t in range(T):
    N, M, L=map(int, input().split())
    arr=[0]*(N+1)
    cnt=0
    for _ in range(M):
        c,v=map(int, input().split())
        arr[c]=v
    preorder(1)
    print(f'#{t+1} {arr[L]}')