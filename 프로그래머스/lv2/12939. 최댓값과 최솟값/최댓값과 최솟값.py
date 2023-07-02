def solution(s):
    answer = 0
    a=list(map(int,s.split(' ')))
    return str(sorted(a)[0])+' '+str(sorted(a)[-1])