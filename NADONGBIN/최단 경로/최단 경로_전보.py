"""
입력 예시
3 2 1
1 2 4
1 3 2
"""
import heapq
import sys

inf = 21e8
n,m,start = map(int, input().split())
arr = [[] for _ in range(n+1)]
distance = [inf]*(n+1)

for _ in range(m):
    s,e,cost= map(int, input().split())
    arr[s].append((e,cost))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in arr[now]:
            cost = dist+i[1]
            if cost <distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

count=0
max_distance = 0
for d in distance:
    if d!=inf:
        count+=1
        max_distance=max(max_distance,d)

print(count-1, max_distance)