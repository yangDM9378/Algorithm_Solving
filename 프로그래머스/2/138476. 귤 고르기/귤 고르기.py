def solution(k, tangerine):
    answer = 0
    dic = {}
    for tang in tangerine:
        if tang not in dic.keys():
            dic[tang] = 1
        else:
            dic[tang] += 1
    sort_dic = sorted(dic.items(), key = lambda x:-x[1])
    num = 0
    for item in sort_dic:
        k -= item[1]
        answer += 1
        if k <= 0: 
            return answer