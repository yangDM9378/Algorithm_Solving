def solution(n, s):
    if s//n ==0:
        return [-1]
    if s%n==0:
        return [s//n]*n
    answer=[]
    k=n-s%n
    print(k)
    answer.append(s//n)
    answer *= k
    for a in range(s%n):
        answer.append(s//n+1)
    
    return answer