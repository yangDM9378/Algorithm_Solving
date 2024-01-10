import heapq
import sys
q = []
N=int(input())
for _ in range(N):
    num = int(sys.stdin.readline())
    if num==0:
        if len(q)==0:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q,num)
