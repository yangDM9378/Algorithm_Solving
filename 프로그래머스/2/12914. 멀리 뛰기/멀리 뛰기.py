def solution(n):
    dp = [0] * (n + 1)
    answer = 0
    if n == 1:
        return 1
    dp[0] = 1
    dp[1] = 2
    dp[2] = 3
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1] % 1234567