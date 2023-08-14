def gems_check(dic_gems):
    if 0 in dic_gems.values():
        return False
    return True

def solution(gems):
    if len(gems)==1:
        return [0,0]
    answer = []
    set_gems = set(gems)
    dic_gems = {gems[0]:1}
    start = 0
    target = 0
    while True:
        if target == len(gems) or start == len(gems):
            break
        if len(dic_gems)<len(set_gems):
            target+=1
            if target == len(gems):
                break
            dic_gems[gems[target]]=dic_gems.get(gems[target],0) +1
        else:
            answer.append([start+1,target+1, target-start])
            if dic_gems[gems[start]] == 1:
                del dic_gems[gems[start]]
            else:
                dic_gems[gems[start]]-=1
            start+=1
    answer.sort(key=lambda x:(x[2],x[0]))
    return [answer[0][0], answer[0][1]]