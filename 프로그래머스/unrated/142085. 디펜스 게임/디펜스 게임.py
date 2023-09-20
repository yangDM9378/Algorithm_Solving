import heapq
def solution(n, k, enemy):
    answer = 0
    hq=[]
    for i in range(len(enemy)):
        heapq.heappush(hq,enemy[i])
        if len(hq) > k:
            n -= heapq.heappop(hq)
        if n<0:
            return i
    return len(enemy)