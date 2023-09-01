def solution(n):
    def hanoi(s,e,m,n):
        if n==1:
            answer.append([s,e])
            return
        hanoi(s,m,e,n-1)
        answer.append([s,e])
        hanoi(m,e,s,n-1)
    answer=[]
    hanoi(1,3,2,n)
    return answer