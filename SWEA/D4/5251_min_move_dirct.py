def dijkstra(start):
    heapq.heappush(heap, (0, start))
    result[start] = 0

    while heap:
        sk, k = heapq.heappop(heap)

        if result[k] < sk: continue
        if k >= N: continue
        for i in arr[k]:
            cost = sk + i[1]
            if cost < result[i[0]]:
                result[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))


import heapq
T=int(input())
for t in range(T):
    N,E=map(int, input().split())
    arr=[[] for _ in range(N)]
    for _ in range(E):
        s,e,w=map(int,input().split())
        arr[s].append((e,w))
    result=[21e8]*(N+1)
    heap=[]
    dijkstra(0)
    print(f'#{t+1} {result[-1]}')

