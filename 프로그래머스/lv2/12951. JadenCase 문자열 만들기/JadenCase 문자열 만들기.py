def solution(s):
    s=' '+s
    answer=''
    for i in range(0, len(s)-1):
        # print(type(s[i+1]))
        k=s[i+1]
        if s[i] == ' ':
            if s[i+1].isdecimal()==False:
                k=s[i+1].upper()
        else:
            k=s[i+1].lower()
        answer += k
        print(answer)
    return answer