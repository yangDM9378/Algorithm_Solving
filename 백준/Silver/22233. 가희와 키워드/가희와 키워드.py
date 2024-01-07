import sys

N, M = map(int, sys.stdin.readline().split())
memo=dict()
for _ in range(N):
    memo[sys.stdin.readline().rstrip()]=1
cnt = N
for _ in range(M):
    post = sys.stdin.readline().rstrip().split(',')
    for word in post:
        if word in memo.keys():
            if memo[word]==1:
                memo[word]-=1
                cnt-=1
    print(cnt)
