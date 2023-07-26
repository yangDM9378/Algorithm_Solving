from collections import deque
def solution(A, B):
    answer = 0
    A=sorted(A)
    B=sorted(B)
    A_q = deque(A)
    B_q = deque(B)
    while A_q:
        A_num=A_q.pop()
        B_num=B_q.pop()
        if A_num<B_num:
            answer+=1
        else:
            B_q.append(B_num)
            B_q.popleft()
    return answer