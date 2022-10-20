import sys
input = sys.stdin.readline

N,M=map(int,input().split())
dic={}
for i in range(1,N+1):
    t=input().rstrip()
    dic[i]=t
    dic[t]=i
for _ in range(M):
    a=input().rstrip()
    if a.isdigit():
        print(dic[int(a)])
    else:
        print(dic[a])