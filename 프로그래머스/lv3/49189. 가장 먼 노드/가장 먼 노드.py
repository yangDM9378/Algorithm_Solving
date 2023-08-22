import heapq
def dijkstra(start):
    q=[]
    heapq.heappush(q, (0, start))
    distance[start]=1
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] <dist:continue
        
        for i in arr[now]:
            cost  = dist + i[1]
            if cost <distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost, i[0]))
def solution(n, edge):
    global distance,arr
    distance = [21e8] * (n+1)
    arr = [[] for _ in range(n+1)]
    for edg in edge:
        a,b =edg[0], edg[1]
        arr[a].append((b,1))
        arr[b].append((a,1))
    dijkstra(1)
    print(distance)
    answer = distance.count(max(distance[1:]))
    return answer