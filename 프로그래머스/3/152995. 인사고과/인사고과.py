def solution(scores):
    answer = 1
    wanho_at,wanho_ex = scores[0]
    scores.sort(key=lambda x:(-x[0],x[1]))
    pass_num = 0
    for score in scores:
        check_at, check_ex = score
        if wanho_at < check_at and wanho_ex < check_ex:
            return -1
        
        if pass_num <= check_ex:
            if wanho_at+wanho_ex < check_at+check_ex:
                answer+=1
            pass_num = check_ex
    return answer