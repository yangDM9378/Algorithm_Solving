from collections import Counter

def solution(topping):
    answer = 0
    cheol = Counter(topping)
    bro = {}
    for topp in topping:
        if len(bro) == len(cheol):
            answer+=1
        if topp not in bro:
            bro[topp]=1
        
        cheol[topp] -=1
        if cheol[topp] ==0:
            del cheol[topp]
    return answer