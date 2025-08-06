from collections import deque
def solution(prices):
    answer = [0] * len(prices)
    q = deque(prices)
    cnt = 0
    while q:
        time = 0
        val = q.popleft()
        for i in range(cnt+1, len(prices)):
            time+=1  
            if prices[i] < val: break
        answer[cnt] = time
        cnt += 1
        
    return answer