# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
# n= int(input())
# f=[0 for i in range(10001)]
# def fibo(n):
#     if n==0: return 0
#     if n==1: return 1
#     f[n] = fibo(n-1)+fibo(n-2)
#     return f[n]
#
# print(fibo(n))


n=int(input())
dp = [0 for _ in range(10001)]
dp[0]=0
dp[1]=1
for i in range(2, n+1):
    dp[i]=dp[i-1] + dp[i-2]
print(dp[n])