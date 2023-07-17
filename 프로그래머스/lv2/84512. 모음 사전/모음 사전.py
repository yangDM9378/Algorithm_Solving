def dfs(level,wo,word):
    global answer, arr,cnt
    if wo == word:
        cnt=answer
        return answer
    if level == 5:
        return
    
    for i in range(5):
        answer+=1
        new_wo = wo+arr[i]
        dfs(level+1, new_wo, word)

def solution(word):
    global answer,arr,cnt
    answer = 0
    cnt=0
    arr=['A','E','I','O','U']
    dfs(0,'',word)
    return cnt