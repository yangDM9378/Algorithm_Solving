def solution(x, y, n):
    dp = [21e1] * (y + 1)
    dp[x] = 0

    for i in range(x + 1, y + 1):
        values = []
        if i - n >= x:
            values.append(dp[i - n] + 1)
        if i % 2 == 0 and i // 2 >= x:
            values.append(dp[i // 2] + 1)
        if i % 3 == 0 and i // 3 >= x:
            values.append(dp[i // 3] + 1)
        if values:
            dp[i] = min(values)

    return int(dp[y]) if dp[y] < 21e1 else -1