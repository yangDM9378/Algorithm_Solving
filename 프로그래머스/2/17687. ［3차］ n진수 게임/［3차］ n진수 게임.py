def convert_num(n, num):
    values = "0123456789ABCDEF"
    n_num = ""
    while (num):
        n_num += values[num % n]
        num = num // n
    return n_num[::-1]

def solution(n, t, m, p):
    num = 0
    answer = "0"
    result = ""
    while (len(answer) < (t+1)*m):
        convert_val = convert_num(n, num)
        answer += convert_val
        num += 1
    
    for i in range(p-1, len(answer), m):
        result += answer[i]
        if len(result) == t:
            break
    return result

