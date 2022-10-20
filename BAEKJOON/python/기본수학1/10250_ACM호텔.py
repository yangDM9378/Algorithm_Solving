T=int(input())
for t in range(T):
    H,W,N=map(int,input().split())
    if (N%H)==0:
        cmd=H
    else:
        cmd=N%H
    if (N%H)==0:
        qkd=(N//H)
    else:
        qkd=(N//H)+1
    print(cmd*100+qkd)
