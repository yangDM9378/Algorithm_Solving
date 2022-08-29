# import sys
# sys.stdin = open("s_input.txt", "r")

T=int(input())
for t in range(T):
    C=[0]*5001
    N=int(input())
    for _ in range(N):
        N_arr=list(map(int, input().split()))
        for k in range(N_arr[0],N_arr[1]+1):
            C[k]+=1
    P=int(input())
    li=[]
    print(f'#{t + 1}', end=' ')
    for _ in range(P):
        C_n=int(input())
        print(C[C_n], end=' ')
    print()