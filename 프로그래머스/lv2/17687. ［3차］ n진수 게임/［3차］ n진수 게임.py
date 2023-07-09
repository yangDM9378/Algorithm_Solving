def n_wlstn(n,i):
    li="0123456789ABCDEF"
    if i == 0:
        return '0'
    n_wls=''
    while i > 0:
        i,mod = divmod(i,n)
        n_wls += li[mod]
    return n_wls[::-1]
    
def solution(n, t, m, p):
    answer = ''
    result = ''
    sum_str=p-1

    for i in range(t*m):
        result += n_wlstn(n,i)
    while True:
        if len(answer) == t:
            break
        answer += result[sum_str]
        sum_str += m

    return answer