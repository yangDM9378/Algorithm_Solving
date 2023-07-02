def solution(clothes):
    answer = 1
    dic={}
    for cloth in clothes:
        dic[cloth[1]]=dic.get(cloth[1],0)+1
    
    for num in dic.items():
        answer *= num[1]+1
    return answer-1