def a_10(a,b):
    for i in range(10):
        for j in range(10):
            arr[a+i][b+j]+=1
    return arr


T=int(input())
arr=[[0]*101 for _ in range(101)]
for _ in range(T):
    a,b=map(int, input().split())
    arr=a_10(a,b)[:]


cnt=0
for i in range(101):
    for j in range(101):
        if arr[i][j]!=0:
            cnt+=1
print(cnt)