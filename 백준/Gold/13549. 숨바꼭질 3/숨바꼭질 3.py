import heapq
N,K = map(int, input().split())
distance = [21e8]*100001

def dijkstra(start):
    distance[start]=0
    hq=[]
    heapq.heappush(hq,(0,start))

    while hq:
        dist, now = heapq.heappop(hq)
        if distance[now] < dist:
            continue
        for idx, time in [(now*2,dist),(now+1,dist+1),(now-1,dist+1)]:
            if 0<=idx<=100000 and distance[idx]>time:
                distance[idx]=time
                heapq.heappush(hq,(time,idx))
dijkstra(N)
print(distance[K])