import heapq

def solution(n, works):
    
    if sum(works) <= n:
        return 0
    works = [-work for work in works]
    heapq.heapify(works)
    for _ in range(n):
        value = heapq.heappop(works)
        value += 1
        heapq.heappush(works, value)
        
    return sum([result**2 for result in works])