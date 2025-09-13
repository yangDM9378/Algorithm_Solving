import heapq
def solution(n, works):
    answer = 0
    hq = []
    for work in works:
        hq.append(-work)
    heapq.heapify(hq)
    while True:
        if n == 0 or len(hq) == 0:break
        n-=1
        pop_num = heapq.heappop(hq)+1
        if pop_num == 0:continue
        heapq.heappush(hq, pop_num)
    for h in hq:
        answer += h**2
    return answer