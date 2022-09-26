import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n,m,r=map(int, input().split())
node=[[] for _ in range(n+1)]
ans=[0]*(n+1)
cur=1

for _ in range(m):
    a,b=map(int, input().split())
    node[a].append(b)
    node[b].append(a)
for k in node:
    k.sort()

def dfs(now):
    global cur
    ans[now]=cur
    for node_v in node[now]:
        if ans[node_v]:
            continue
        cur+=1
        dfs(node_v)
dfs(r)
for i in ans[1:]:
    print(i)