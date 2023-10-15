def dfs(idx, ssum):
    global answer
    if idx >= n:
        answer = max(answer, ssum)
        return
    if idx+t_arr[idx]<=n:
        dfs(idx+t_arr[idx], ssum+p_arr[idx])
    dfs(idx+1, ssum)
n=int(input())
t_arr=[0]*n
p_arr=[0]*n
answer=0
for i in range(n):
    t_arr[i],p_arr[i] = map(int, input().split())
dfs(0,0)
print(answer)