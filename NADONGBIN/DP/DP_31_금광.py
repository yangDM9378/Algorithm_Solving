"""
입력예시
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""
T=int(input())
for _ in range(T):
    n, m=map(int, input().split())
    arr=[[0]*m for _ in range(n)]
    li=list(map(int, input().split()))
    for i in range(len(li)):
        arr[i//m][i%m]=li[i]

    for j in range(1,m):
        for i in range(n):
            if i == 0:
                arr[i][j] += max(arr[i][j-1], arr[i+1][j-1])
            elif i == n-1:
                arr[i][j] += max(arr[i-1][j-1], arr[i][j-1])
            else:
                arr[i][j] += max(arr[i-1][j-1], arr[i][j-1], arr[i+1][j-1])
    result = -1
    for i in range(n):
        if result < arr[i][m-1]:
            result = arr[i][m-1]
    print(result)