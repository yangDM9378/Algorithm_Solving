def solution(stones, k):
    answer = -1
    s = 0
    e = max(stones)
    while s<=e:
        flag = True
        m = (s+e)//2
        cnt =0 
        for stone in stones:
            if stone - m <=0:
                cnt +=1
                if cnt==k:
                    flag = False
                    break
            else:
                cnt = 0
        if flag:
            s = m+1
            answer= max(answer, m+1)
        else:
            e = m-1
    return answer