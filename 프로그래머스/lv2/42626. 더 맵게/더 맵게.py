import heapq

def solution(scoville, K):
    cnt=0
    heapq.heapify(scoville)
    while True:
        a=heapq.heappop(scoville)
        if len(scoville)==0 and a<=K:
            cnt=-1
            break
        if a>=K:
            break
        if a<K:
            cnt+=1
            b=heapq.heappop(scoville)
            scov = a+(b*2)
            heapq.heappush(scoville,scov)
    return cnt