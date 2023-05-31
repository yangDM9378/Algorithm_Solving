from collections import deque
def bfs(n,m):
    global cnt
    q=deque()
    q.append(n)
    while q:
        n = q.popleft()
        if n==m:
            print(dist[n])
            break
        for nx in (n-1, n+1, n*2):
            if 0<=nx<=100000 and dist[nx]==0:
                dist[nx] = dist[n] +1
                q.append(nx)


n,m = map(int, input().split())
dist = [0]*(100001)
cnt=0
bfs(n,m)

