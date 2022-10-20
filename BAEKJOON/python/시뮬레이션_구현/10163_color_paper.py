def  ea(a,b,str_1):
    for i in range(c):
        for j in range(d):
            arr[a+i][b+j]=str_1
    return arr
arr=[[0]*1002 for _ in range(1002)]
T=int(input())
li=[i for i in range(1,T+1)]
for k in range(T):
    a,b,c,d=map(int, input().split())
    arr=ea(a,b,li[k])
for z in li:
    cnt=0
    for i in range(1002):
        for j in range(1002):
            if arr[i][j]==z:
                cnt+=1
    print(cnt)

