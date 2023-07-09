"""
입력예시
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
"""
import heapq
n,m = map(int, input().split())

distance = [21e8]*(n+1)

arr = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    arr[a].append((b,1))
    arr[b].append((a,1))

def dijkstra(start):
    q=[]
    heapq.heappush(q, (0,start))
    distance[start]=1
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:continue

        for i in arr[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)
max_result = 0
max_distance = 0
for i in range(1,len(distance)):
    if distance[i]>max_distance:
        max_result=i
        max_distance=distance[i]

print(max_result)
print(max_distance)
print(distance.count(max_distance))