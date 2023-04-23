from collections import deque

def bfs(a,b):
    q=deque()
    q.append((a,0))
    while q:
        k, cnt = q.popleft()
        visited[k] = True
        for i in arr[k]:
            if i == b:
                return cnt+1
            if not visited[i]:
                q.append((i, cnt+1))
    return -1

n=int(input())
a,b = map(int, input().split())
m=int(input())
arr=[[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    x,y = map(int, input().split())
    arr[y].append(x)
    arr[x].append(y)
print(bfs(a,b))