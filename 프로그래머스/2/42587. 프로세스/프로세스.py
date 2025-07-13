from collections import deque
import heapq

def solution(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    max_heap = [-p for p in priorities]
    heapq.heapify(max_heap)

    order = 0
    while queue:
        idx, priority = queue.popleft()
        
        if priority == -max_heap[0]:
            heapq.heappop(max_heap)
            order += 1
            if idx == location:
                return order
        else:
            queue.append((idx, priority)) 
