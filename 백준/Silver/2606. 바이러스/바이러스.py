def dfs(start):
    global cnt
    used[start]=1
    for i in arr[start]:
        if used[i]==1:continue
        dfs(i)
        cnt+=1

n=int(input())
t=int(input())
arr = [[] for _ in range(n+1)]
used=[0]*(n+1)
for _ in range(t):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

cnt=0
dfs(1)
print(cnt)