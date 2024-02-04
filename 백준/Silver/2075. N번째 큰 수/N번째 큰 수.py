import heapq

n = int(input())
hq = []
for _ in range(n):
    arr = map(int, input().split())
    for num in arr:
        if len(hq) < n:
            heapq.heappush(hq, num)
        else:
            if hq[0] < num:
                heapq.heappop(hq)
                heapq.heappush(hq, num)

print(heapq.heappop(hq))
