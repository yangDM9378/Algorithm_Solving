def solution(brown, yellow):
    answer = []
    for i in range(1, yellow // 2+1):
        if yellow % i == 0:
            rk = yellow // i
            if (i+rk) *2 +4 == brown:
                break
    if yellow == 1:
        return [3,3]
    answer.append(max(i,rk)+2)
    answer.append(min(i,rk)+2)
    return answer