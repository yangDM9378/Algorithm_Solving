from collections import deque
def solution(priorities, location):
    answer = 0
    sorted_priorities = sorted(priorities, reverse=True)
    q = deque()
    sq = deque(sorted_priorities)
    for i in range(len(priorities)):
        q.append([i,priorities[i]])

    while sq:
        val = sq.popleft()
        while q:
            idx, priority = q.popleft()
            if val == priority:
                answer+=1
                break
            else:
                q.append([idx, priority])
        if location == idx:
            break
    return answer