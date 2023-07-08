def solution(msg):
    answer = []
    dic={}
    for i in range(26):
        dic[chr(i+65)]=i+1
    start,end = 0,1
    cnt=27
    _str=''
    while end < len(msg)+1:
        _str=msg[start:end]
        if _str in dic.keys():
            end +=1
        else:
            answer.append(dic[_str[:-1]])
            dic[_str]=cnt
            cnt+=1
            start=end-1
    answer.append(dic[_str])
    return answer