from collections import defaultdict 
        
def solution(clothes):
    dic = defaultdict(list)
    for clothe in clothes:
        dic[clothe[1]].append(clothe[0])
    cnt = 1
    for key, value in dic.items():
        cnt *= len(value)+1
    return cnt-1