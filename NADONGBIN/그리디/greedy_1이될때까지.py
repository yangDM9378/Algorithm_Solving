"""
입력예시
25 5
"""

N,K = map(int, input().split())
cnt = 0
while True:
    if N == 1:
        break
    if N % K == 0:
        N = N//K
        cnt+=1
    else:
        target=(N//K)*K
        if target==0:
            cnt+=N
            N=1
        else:
            cnt+=(N-target)
            N = target
print(cnt)