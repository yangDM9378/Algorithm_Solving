def solution(m, n, puddles):
    answer = 0
    arr = [[0] * m for _ in range(n)]
    arr[0][0]=1
    for puddle in puddles:
        arr[puddle[1]-1][puddle[0]-1]=-1
    for i in range(n):
        for j in range(m):
            if arr[i][j] != -1:
                if i>0 and arr[i-1][j] !=-1:
                    arr[i][j]+=arr[i-1][j]
                if j>0 and arr[i][j-1] !=-1:
                    arr[i][j]+=arr[i][j-1]
    return arr[n-1][m-1]%1000000007