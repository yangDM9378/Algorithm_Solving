from copy import deepcopy
def check_id(uid, ban_id):
    for i in range(len(uid)):
        if ban_id[i]=='*':continue
        if ban_id[i]!=uid[i]:
            return False
    return True

def dfs(level, banned_id, arr):
    global result, results,dic
    if level == len(banned_id):
        if len(set(result)) == len(banned_id):
            sort_result = sorted(result)
            if sort_result not in results:
                results.append(deepcopy(sort_result))
        return 
        
    for i in arr[level]:
        if dic[i]==1:continue
        dic[i]=1
        result.append(i)
        dfs(level+1, banned_id, arr)
        result.pop()
        dic[i]=0
        
        
def solution(user_id, banned_id):
    global result, results,dic
    answer = 0
    arr=[[] for _ in range(len(banned_id))]
    result = []
    results = []
    dic={}
    for idx in range(len(banned_id)):
        ban_id=banned_id[idx]
        for uid in user_id:
            if len(uid) == len(ban_id):
                checked_id = check_id(uid, ban_id)
                if checked_id:
                    arr[idx].append(uid)
                    dic[uid]=0
    print(dic)
    dfs(0, banned_id, arr)
    return len(results)