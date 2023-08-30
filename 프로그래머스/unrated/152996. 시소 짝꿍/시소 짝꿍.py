# def solution(weights):
#     answer = 0
#     for i in range(len(weights)-1):
#         checked = [0]*4001
#         for k in [2,3,4]:
#             checked[weights[i]*k]=1
#         for j in range(i+1, len(weights)):
#             for k in [2,3,4]:
#                 if checked[weights[j]*k]==1:
#                     answer+=1
#                     break    
#     return answer

from collections import Counter


def solution(weights):
    answer = 0
    counter = Counter(weights)
    for k,v in counter.items():
        if v>=2:
            # 전체 갯수 중 2개 뽑는 경우의 수
            answer+= v*(v-1)//2
    weights = set(weights) 
    
    for w in weights:
        if w*2/3 in weights:
            answer+= counter[w*2/3] * counter[w]
        if w*2/4 in weights:
            answer+= counter[w*2/4] * counter[w]
        if w*3/4 in weights:
            answer+= counter[w*3/4] * counter[w]
    return answer
