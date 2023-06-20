"""
입력예시
5 8 3
2 4 5 4 6
"""

# M이 작을때는 사용가능하지만 M이 엄청 클때 시간초과
N,M,K = map(int, input().split())
arr =list(map(int, input().split()))
arr=sorted(arr)
max_first=arr[-1]
max_second=arr[-2]
cnt=0
dupli_cnt=0

while True:
    if M == 0:
        break

    if dupli_cnt!=0:
        cnt += max_first
        dupli_cnt -= 1
        M -= 1
    else:
        cnt += max_second
        dupli_cnt = K
        M -= 1
print(cnt)

# solution M이 엄청 클때
N,M,K = map(int, input().split())
arr =list(map(int, input().split()))
arr=sorted(arr)
max_first=arr[-1]
max_second=arr[-2]
print((max_first*K+max_second)*(M//(K+1))+(max_first*(M%(K+1))))
