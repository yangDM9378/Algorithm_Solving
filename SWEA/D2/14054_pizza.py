def zez(pizza):
    while q:
        if len(q)==1:
            return q[0][1]
        q[0][0]=q[0][0]//2
        if q[0][0]==0:
            if len(pizza)!=0:
                q.pop(0)
                q.append(pizza.pop(0))
            else:
                q.pop(0)
        else:
            q.append(q.pop(0))



T=int(input())
for t in range(T):
    n,m=map(int, input().split())
    arr=list(map(int, input().split()))
    num=[i for i in range(1,m+1)]
    pizza=[0]*m
    for z in range(m):
        pizza[z]=[arr[z],num[z]]
    q=[]
    for i in range(n):
        q.append(pizza.pop(0))
    print(f'#{t+1} {zez(pizza)}')

