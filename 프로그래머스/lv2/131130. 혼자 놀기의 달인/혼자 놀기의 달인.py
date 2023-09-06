def solution(cards):
    used = [0]*(len(cards)+1)
    cards.insert(0,0)
    answer=[]
    for i in range(1,len(cards)):
        if used[i]==1:continue
        arr=[]
        used[i]=1
        value = cards[i]
        arr.append(i)
        while True:
            if used[value]==1:break
            used[value]=1
            arr.append(value)
            value = cards[value]
        answer.append(len(arr))
    answer.sort()
    if len(answer)==1:
        return 0
    return answer[-1]*answer[-2]