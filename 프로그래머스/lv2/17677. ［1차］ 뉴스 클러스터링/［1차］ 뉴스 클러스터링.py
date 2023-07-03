def solution(str1, str2):
    answer = 0
    dic_str1={}
    dic_str2={}
    for i in range(len(str1)-1):
        check_str = str1[i:i+2]
        if check_str.isalpha():
            dic_str1[check_str.upper()]=dic_str1.get(check_str.upper(),0)+1
    for i in range(len(str2)-1):
        check_str = str2[i:i+2]
        if check_str.isalpha():
            dic_str2[check_str.upper()]=dic_str2.get(check_str.upper(),0)+1
    cnt=0
    for _str in dic_str1.keys():
        if _str in dic_str2.keys():
            cnt+=min(dic_str1[_str],dic_str2[_str])
    keys_arr=dic_str1.keys() | dic_str2.keys()
    union_cnt = 0
    for key in keys_arr:
        dic_str1[key]=dic_str1.get(key, 0)
        dic_str2[key]=dic_str2.get(key, 0)
        union_cnt += max(dic_str1[key], dic_str2[key])
    print(cnt, union_cnt)
    if union_cnt == 0:
        return 1 * 65536
    answer=cnt/union_cnt
    return int(answer*65536)