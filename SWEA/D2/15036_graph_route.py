import sys
sys.stdin = open("15036.txt", "r")

def dfs(now):
    global li
    li.append(now)
    for i in range(v):
        if z[now][i]==1 and used[i]==0:
            used[now]=1
            dfs(i)
            used[now]=0



T=int(input())
for t in range(T):
    v,e=map(int, input().split())
    z=[[0]*v for _ in range(v)]
    for _ in range(e):
        i,j=map(int,input().split())
        z[i-1][j-1]=1
    s,g=map(int,input().split())
    li = []
    used=[0]*v
    used[s-1]=1
    dfs(s-1)
    if g-1 in li:
        print(f'#{t+1} 1')
    else:
        print(f'#{t+1} 0')

