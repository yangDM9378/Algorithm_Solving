def solution(s):
    answer = ''
    checked = True
    # A : 65 ~ 90 a: 97 ~122
    for i in s:
        if ord(i) == 32:
            checked=True
            answer += " "
            continue
        if checked and (97 <= ord(i) <= 122):
            answer += i.upper()
        elif not checked and (65 <= ord(i) <= 90):
            answer += i.lower()
        else:
            answer += i
        checked=False
    
    return answer