def solution(n):
    ssum = 0
    cnt = 0
    s = 1
    for i in range(1,n+1):
        ssum += i
        if ssum == n:
            cnt+=1
        if ssum >= n:
            for j in range(s,i+1):
                ssum -= j
                if ssum == n:
                    cnt+=1
                if ssum < n:
                    s=j+1
                    break

    return cnt