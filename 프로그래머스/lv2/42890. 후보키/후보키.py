from itertools import combinations
def solution(relation):
    check_arr=[i for i in range(len(relation[0]))]
    result = []
    for k in range(1,len(relation)):
        check_idxs = list(combinations(check_arr,k))
        for check_idx in check_idxs:
            check_dic = {}
            for relate in relation:
                word=''
                for idx in check_idx:
                    word += relate[idx]
                check_dic[word]=check_dic.get(word,0)
                check_dic[word]+=1
            flag = True
            for value in check_dic.values():
                if value != 1:
                    flag=False
                    break
            if flag:
                result.append(check_idx)
    answer=set(result)           
    for i in range(len(result)):
        for j in range(i+1, len(result)):
            if set(result[i]).issubset(set(result[j])):
                answer.discard(result[j])
        

    return len(answer)