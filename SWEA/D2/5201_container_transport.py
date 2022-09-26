T=int(input())
for k in range(T):
    n,m=map(int, input().split())
    w=list(map(int, input().split()))
    t=list(map(int, input().split()))
    cnt=0
    w.sort(reverse=True)
    t.sort(reverse=True)
    temp=0
    for i in w:
        for j in range(temp,len(t)):
            if i<=t[j]:
                cnt+=i
                temp+=1
                break
    print(f'#{k+1} {cnt}')