def findboss(member):
    global arr
    if arr[member]==0:
        return member
    ret=findboss(arr[member])
    return ret

def union(a,b):
    global arr
    aboss=findboss(a)
    bboss=findboss(b)
    if aboss==bboss:
        return
    arr[bboss]=aboss

T=int(input())
for t in range(T):
    N,M=map(int,input().split())
    li=list(map(int, input().split()))
    arr=[0]*(N+1)
    for i in range(M):
        a=li.pop(0)
        b=li.pop(0)
        union(a,b)
    boss_li=[0]*(N+1)
    for i in range(len(arr)):
        if arr[i]!=0 and arr[arr[i]]==0:
            boss_li[arr[i]]=1
    cnt=0
    for i in range(len(boss_li)):
        if i==1:
            cnt+=1
    k=arr.count(0)
    print(f'#{t+1} {k-cnt}')
