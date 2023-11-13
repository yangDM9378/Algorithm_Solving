from collections import deque

def dfs(F,S,G,U,D):
    cnt=0
    q=deque()
    q.append((S,cnt))
    while q:
        current,cnt=q.popleft()
        if current == G:
            return cnt
        for i in [U,-D]:
            next = current+i
            if 1<=next<=F and used[next]==0:
                q.append((next,cnt+1))
                used[next] = 1
    return 'use the stairs'
F,S,G,U,D = map(int, input().split())
used=[0]*(F+1)
print(dfs(F,S,G,U,D))