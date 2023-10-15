# def dfs(idx, ssum):
#     global answer
#     if idx >= n:
#         answer = max(answer, ssum)
#         return
#     if idx+t_arr[idx]<=n:
#         dfs(idx+t_arr[idx], ssum+p_arr[idx])
#     dfs(idx+1, ssum)
# n=int(input())
# t_arr=[0]*n
# p_arr=[0]*n
# answer=0
# for i in range(n):
#     t_arr[i],p_arr[i] = map(int, input().split())
# dfs(0,0)
# print(answer)

# dp풀이
n=int(input())
t_arr=[0]*n
p_arr=[0]*n
answer=0
for i in range(n):
    t_arr[i],p_arr[i] = map(int, input().split())
dp=[0]*(n+1)
for i in range(n-1, -1, -1):
    if i+t_arr[i] <= n:
        dp[i] = max(dp[i+t_arr[i]]+p_arr[i], dp[i+1])
    else:
        dp[i]=dp[i+1]
print(dp[0])