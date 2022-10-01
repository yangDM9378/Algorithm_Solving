def findboss(member):
    if arr[member]=='0':
        return member
    ret=findboss(arr[member])
    arr[member]=ret
    return ret

def union(y,x):
    yboss,xboss=findboss(y),findboss(x)
    if yboss==xboss: return False
    arr[xboss]=yboss
    return True

T=int(input())
for t in range(T):
    k,n=map(int,input().split())
    lst=[]
    for i in range(n):
        a, b, cost = map(int, input().split())
        z=[cost, a, b]
        lst.append(z)
    lst.sort()
    arr=['0']*(k+1)
    answer=0
    cnt=0
    for i in lst:
        if union(i[1],i[2])==True:
            answer+=i[0]
    print(f'#{t+1} {answer}')