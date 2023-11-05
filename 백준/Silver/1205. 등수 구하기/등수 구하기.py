n, new_score, p = map(int,input().split())


sam_cnt = 0
result = n+1
if n==0:
    print(1)
else:
    scores = list(map(int, input().split()))
    if n==p and scores[-1]>=new_score:
        print(-1)
    else:
        for i in range(n):
            if scores[i]<=new_score:
                result = i+1
                break
        print(result)