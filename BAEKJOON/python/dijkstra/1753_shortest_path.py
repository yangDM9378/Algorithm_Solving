import heapq
V,E=map(int, input().split())
K=int(input())
arr=[[] for _ in range(V+1)]
for _ in range(E):
    u,v,w=map(int,input().split())
    arr[u].append((v,w))
result=[21e8]*(V+1)
heap=[]
def dijkstra(start):
    heapq.heappush(heap,(0,start))
    result[start]=0
    while heap:
        sk,k=heapq.heappop(heap)
        if result[k]<sk:continue
        for i in arr[k]:
            cost=sk+i[1]
            if cost<result[i[0]]:
                result[i[0]]=cost
                heapq.heappush(heap,(cost, i[0]))
dijkstra(K)
for i in range(1,len(result)):
    if result[i]==21e8:
        print('INF')
    else:
        print(result[i])