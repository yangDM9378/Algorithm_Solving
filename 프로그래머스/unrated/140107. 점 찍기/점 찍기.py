def solution(k, d):
    answer=0
    for a in range(0, d+1, k):
        max_b=int((d**2 - a**2)**0.5)
        answer+=(max_b//k)+1
    return answer