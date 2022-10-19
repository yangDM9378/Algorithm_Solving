T=int(input())
for _ in range(T):
    k=int(input())
    n=int(input())
    li=[[0]*n for _ in range(k+1)]
    for i in range(k+1):
        li[i][0]=1
    for i in range(0,n):
        li[0][i]=i+1
    for i in range(1,k+1):
        for j in range(1,n):
            li[i][j]=li[i][j-1]+li[i-1][j]
    print(li[-1][-1])