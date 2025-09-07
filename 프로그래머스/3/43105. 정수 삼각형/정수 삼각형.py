def solution(triangle):
    answer = 0
    dp = []
    for i in range(len(triangle)):
        dp.append([0]*(i+1))
    for i in range(len(triangle[-1])):
        dp[-1][i] = triangle[-1][i]
    for y in range(len(triangle)-2,-1,-1):
        for x in range(len(triangle[y])):
            dp[y][x] = max(triangle[y][x]+dp[y+1][x], triangle[y][x]+dp[y+1][x+1])
    return dp[0][0]