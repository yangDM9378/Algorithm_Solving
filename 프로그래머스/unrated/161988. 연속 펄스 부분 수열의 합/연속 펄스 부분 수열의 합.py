def solution(sequence):
    answer=0
    for i in range(0,len(sequence),2):
        sequence[i]*=-1
    min_result=0
    max_result=0
    for i in range(0, len(sequence)):
        num = sequence[i]
        min_result=min(num, num+min_result)
        max_result=max(num, num+max_result)
        answer = max(answer,abs(min_result),abs(max_result))
    return answer 