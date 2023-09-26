from collections import Counter
def solution(n, results):
    arr = [[0]*(n+1) for _ in range(n+1)]
    for win,loss in results:
        arr[win][loss] = 1
        arr[loss][win] = -1
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if arr[i][j] == 0:
                    if arr[i][k] == 1 and arr[k][j] == 1:
                        arr[i][j] = 1
                    elif arr[i][k] == -1 and arr[k][j] == -1:
                        arr[i][j] = -1
    answer=0
    for i in range(1,n+1):
        if Counter(arr[i])[0] == 2:
            answer += 1
    return answer