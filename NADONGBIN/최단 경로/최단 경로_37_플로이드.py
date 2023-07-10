"""
입력예시
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
"""

n=int(input())
arr = [[21e8]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    arr[i][i]=0
m=int(input())

for _ in range(m):
    a,b,c = map(int, input().split())
    if arr[a][b] > c:
        arr[a][b]=c

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            arr[i][j]= min(arr[i][j], arr[i][k]+arr[k][j])

for i in range(1,n+1):
    for j in range(1, n+1):
        print(arr[i][j],end=' ')
    print()