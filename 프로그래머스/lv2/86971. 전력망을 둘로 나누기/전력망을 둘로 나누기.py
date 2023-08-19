def dfs(start,used):
    global arr,cnt
    for i in range(len(arr[start])):
        if arr[start][i]==1 and used[i]==0:
            used[i]=1
            cnt+=1
            dfs(i,used)

def solution(n, wires):
    global arr,cnt
    answer = -1
    arr =[[0]*(n+1) for _ in range(n+1)]
    for wire in wires:
        a,b = wire[0],wire[1]
        arr[a][b]=1
        arr[b][a]=1
    min_cnt = 21e8
    for wire in wires: 
        a,b = wire[0], wire[1]
        used=[0]*(n+1)
        used[a],used[b]=1,1
        cnt=1
        dfs(a,used)
        a_cnt = cnt
        used=[0]*(n+1)
        used[a],used[b]=1,1
        cnt=1
        dfs(b,used)
        b_cnt = cnt
        if min_cnt > abs(a_cnt-b_cnt):
            min_cnt = abs(a_cnt-b_cnt)

    return min_cnt