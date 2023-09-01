import heapq
def dijkstra(s,e):
    global arr
    n=len(arr)
    distance = [21e8] * n
    q=[]
    heapq.heappush(q,(0,s))
    distance[s]=0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist:continue
        for i in arr[now]:
            cost=dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return distance[e]

def solution(n, s, a, b, fares):
    global arr
    answer = 0
    arr = [[] for _ in range(n+1)]
    for fare in fares:
        arr[fare[0]].append((fare[1],fare[2]))
        arr[fare[1]].append((fare[0],fare[2]))
    sa=dijkstra(s,a)
    sb=dijkstra(s,b)
    cost =sa+sb
    for i in range(n+1):
        cost=min(cost, dijkstra(s,i)+dijkstra(i,a)+dijkstra(i,b))
    
    return cost