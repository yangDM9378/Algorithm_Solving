"""
입력 예시 1
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

입력 예시 2
4 2
1 3
2 4
3 4
"""

n,m = map(int, input().split())
arr=[[21e8]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            arr[i][j]=0
for _ in range(m):
    a,b = map(int, input().split())
    arr[a][b]=1
    arr[b][a]=1

x,k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            arr[a][b] = min(arr[a][b], arr[a][k]+arr[k][b])

distance = arr[1][k] + arr[k][x]

if distance >= 21e8:
    print(-1)
else:
    print(distance)