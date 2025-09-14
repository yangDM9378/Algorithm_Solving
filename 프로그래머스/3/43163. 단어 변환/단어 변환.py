def chk_rule(pre_word, post_word):
    cnt = 0
    for i in range(len(pre_word)):
        if pre_word[i] != post_word[i]:
            cnt+=1
    return True if cnt == 1 else False

def dfs(begin, target, cnt, words):
    global result, used
    if begin == target:
        result = min(result, cnt)
        return
    
    for idx in range(len(words)):
        if chk_rule(begin, words[idx]) and used[idx] != 1:
            used[idx] = 1
            dfs(words[idx], target, cnt+1, words)
            used[idx] = 0
    return

def solution(begin, target, words):
    global result, used
    result = 21e9
    cnt = 0
    used = [0]*len(words)
    dfs(begin, target, cnt, words)
    return result if result != 21e9 else 0