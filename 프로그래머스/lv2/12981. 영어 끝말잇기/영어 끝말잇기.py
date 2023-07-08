from collections import deque
def solution(n, words):
    answer = []
    cnt=1
    result=[]
    check=0
    q = deque(words)
    pre_word = q.popleft()
    result.append(pre_word)
    for word in q:
        cnt+=1
        if pre_word[-1] != word[0]:
            check=1
            break
        elif len(word)==1:
            check=1
            break
        elif word in result:
            check=1
            break
        result.append(word)
        pre_word=word
    if check == 0:
        return [0,0]
    else:
        a=cnt%n
        b=cnt//n
        if a==0:
            a=n
        if cnt/n > cnt//n:
            b=b+1
        
        return [a,b]