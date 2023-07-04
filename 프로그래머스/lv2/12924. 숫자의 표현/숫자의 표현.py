def solution(n):
    start=1
    plus=1
    result = 0
    cnt=0
    while True:
        print(result)
        if start == n:
            break
        if result == n:
            cnt+=1
            print('cnt---')
            result-=start
            start+=1
        elif result > n:
            result = result-start
            start+=1
        elif result < n:
            print(plus)
            result = result + plus
            plus+=1
    return cnt+1