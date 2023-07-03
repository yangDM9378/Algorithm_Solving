def solution(want, number, discount):
    answer = 0
    dic={}
    for i in range(len(number)):
        dic[want[i]]=number[i]
    
    for j in range(10):
        if discount[j] in dic.keys():
            dic[discount[j]] -=1
    cnt=0
    for i in range(len(discount)-9):
        if all(value <= 0 for value in dic.values()):
            cnt+=1
        if discount[i] in dic.keys():
            dic[discount[i]] +=1

        if i+10 < len(discount):
            if discount[i+10] in dic.keys():
                dic[discount[i+10]] -=1
    return cnt
            
        
