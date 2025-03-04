from collections import deque
def solution(n, words):
    pre_li = []
    q = deque(words)
    pre_word = q.popleft()
    pre_li.append(pre_word)
    cnt=1
    while q:
        cnt+=1
        word = q.popleft()
        if word[0] != pre_word[-1]:
            num = n if cnt % n == 0 else cnt % n
            table = cnt // n if cnt % n == 0  else cnt // n + 1
            return [num , table] 
        if word in pre_li:
            num = n if cnt % n == 0 else cnt % n
            table = cnt // n if cnt % n == 0  else cnt // n + 1
            return [num , table]
        pre_word = word
        pre_li.append(word)
    return [0,0]