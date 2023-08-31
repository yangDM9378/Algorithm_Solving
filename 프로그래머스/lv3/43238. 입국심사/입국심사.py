def solution(n, times):
    answer=0
    l, r = 0, max(times)*n+1
    while l <= r:
        mid =(l+r)//2
        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                break
        
        if people < n:
            l=mid+1
        else:
            answer=mid
            r=mid-1
    return answer