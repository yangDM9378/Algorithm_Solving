from collections import deque
def solution(order):
    answer = 0
    stack = [i for i in range(1,len(order)+1)]
    q = deque(stack)
    i = 0
    assist = []
    while True:
        if len(q)==0:
            break
        if assist and assist[-1]==order[i]:
            i+=1
            assist.pop()
            answer+=1
            continue
        if q[0] != order[i]:
            assist.append(q.popleft())
        else:
            q.popleft()
            answer+=1
            i+=1
            continue

    while assist:
        print(order[i])
        if order[i]!=assist[-1]:
            break
        answer+=1
        assist.pop()
        i+=1  
    return answer