import sys
N, M = map(int, sys.stdin.readline().split())
scores=[]
for _ in range(N):
    scores.append(sys.stdin.readline().split())

for _ in range(M):
    num = int(sys.stdin.readline())
    start = 0
    end = N-1
    while True:
        mid = (start + end) // 2
        if start >= end:
            print(scores[mid][0])
            break
        if int(scores[mid][1]) < num:
            start=mid+1
        else:
            end=mid