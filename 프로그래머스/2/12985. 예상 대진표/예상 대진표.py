import math
def solution(n,a,b):
    answer = 0
    A=min(a,b)
    B=max(a,b)
    while True:
        answer += 1
        if (A+1) == B and (A % 2 == 1):
            return answer
        A = math.ceil(A/2)
        B = math.ceil(B/2)
    return answer