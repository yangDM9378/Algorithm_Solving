n,m,v = map(int, input().split())
arr = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    arr[a][b] = 1
    arr[b][a] = 1

used = [0]*(n+1)

result = []
def dfs(v):
    used[v]=1
    print(v, end=' ')
    for i in range(1, n+1):
        if arr[v][i]==1 and used[i]==0:
            dfs(i)
dfs(v)
print()
from collections import deque
used = [0]*(n+1)
def bfs(v):
    q=deque()
    q.append(v)
    used[v] = 1
    while q:
        s = q.popleft()
        print(s, end = ' ')
        for i in range(1,n+1):
            if arr[s][i]==1 and used[i] == 0:
                q.append(i)
                used[i]=1
bfs(v)