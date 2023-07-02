def solution(s):
    cnt_0=0
    result = 0
    while True:
        if len(s)==1:
            break
        result += 1
        cnt_0 += s.count('0')
        s=s.count('1')
        s=bin(int(s))[2:] 
    return [result,cnt_0]