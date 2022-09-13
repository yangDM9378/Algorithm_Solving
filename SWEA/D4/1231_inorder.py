def inorder(now):
    if now>len(arr)-1:
        return
    inorder(now*2)
    print(arr[now], end='')
    inorder(now*2+1)


for t in range(10):
    N=int(input())
    arr=['']*(N+1)
    for i in range(N):
        w=list(map(str, input().split()))
        arr[int(w[0])]=w[1]
    print(f'#{t+1} ', end='')
    inorder(1)
    print()

