T=int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())
    arr = [[0] * k for _ in range(n)]
    times = [0] * n
    cnt = [0] * n
    for M in range(m):
        i, j, s =map(int, input().split())
        arr[i-1][j-1]=max(arr[i-1][j-1],s)
        cnt[i-1]+=1
        times[i-1]=M+1
    scores = []
    for i in range(n):
        scores.append(sum(arr[i]))
    total_arr = []
    for i in range(n):
        total_arr.append([])
        total_arr[i].append(i+1)
        total_arr[i].append(scores[i])
        total_arr[i].append(cnt[i])
        total_arr[i].append(times[i])

    total_arr.sort(lambda x:(-x[1],x[2],x[3]))
    for i in range(n):
        if total_arr[i][0]==t:
            result = i+1
    print(result)