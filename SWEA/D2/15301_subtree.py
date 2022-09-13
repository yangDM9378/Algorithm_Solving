T=int(input())
def preorder(n):
    global cnt
    if n:
        cnt+=1
        preorder(ch1[n])
        preorder(ch2[n])
for t in range(T):
    E,N=map(int,input().split())
    arr=list(map(int, input().split()))
    ch1=[0]*(E+2)
    ch2=[0]*(E+2)
    for i in range(E):
        p,c=arr[i*2],arr[i*2+1]
        if ch1[p]==0:
            ch1[p]=c
        else:
            ch2[p]=c
    cnt=0
    preorder(N)
    print(f'#{t+1} {cnt}')