N,M=map(int,input().split())
arr=set(input() for _ in range(N))
cnt=0
for _ in range(M):
    a= input()
    if a in arr:
        cnt+=1
print(cnt)