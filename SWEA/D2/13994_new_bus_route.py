T= int(input())
for t in range(T):
    N=int(input())
    z=[0]*1001
    for _ in range(N):
        C, A, B=map(int, input().split())
        z[A]+=1
        z[B]+=1
        if C==1:
            for i in range(A+1,B):
                z[i]+=1
        elif C==2:
            if A%2==0:
                for i in range(A+1,B):
                    if i%2==0:
                        z[i]+=1
            else:
                for i in range(A+1,B):
                    if i%2==1:
                        z[i]+=1
        else:
            if A%2==0:
                for i in range(A+1,B):
                    if i%4==0:
                        z[i]+=1
            else:
                for i in range(A+1,B):
                    if i%3==0 and i%10!=0:
                        z[i]+=1
    print(f'#{t+1} {max(z)}')





