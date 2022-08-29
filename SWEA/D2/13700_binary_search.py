T=int(input())

def binary(l,r,k):
    cnt = 0
    while (1):
        m=int((l+r)/2)

        if k>m:
            l=m+1
        elif k<m:
            r=m-1
        else:
            return cnt
        cnt+=1


for t in range(T):
    r,ka,kb=map(int,input().split())
    cnt_a=binary(1,r,ka)
    cnt_b=binary(1,r,kb)
    if cnt_a==cnt_b:
        print(f'#{t+1} {0}')
    elif cnt_a>cnt_b:
        print(f'#{t+1} B')
    else:
        print(f'#{t+1} A')