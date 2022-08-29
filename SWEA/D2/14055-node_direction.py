def bfs(s,g):
    visited = [0]*(V)
    q=[]
    q.append(s)
    visited[s]=1
    while q:
        s=q.pop(0)
        for w in adjlist[s]:
            if visited[w]==0:
                q.append(w)
                visited[w]=visited[s]+1
    if visited[g]-1<0:
        return 0
    return visited[g]-1

T=int(input())
for t in range(T):
    V,E=map(int, input().split())
    adjlist=[[] for _ in range(V)]
    for _ in range(E):
        a,b=map(int, input().split())
        adjlist[a-1].append(b-1)
        adjlist[b-1].append(a-1)
    S,G=map(int, input().split())
    S,G=S-1,G-1
    result=bfs(S,G)
    print(f'#{t + 1} {result}')
