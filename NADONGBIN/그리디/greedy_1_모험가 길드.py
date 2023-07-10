"""
입력 예시
5
2 3 1 2 2
"""

n=int(input())
arr = list(map(int, input().split()))
arr.sort()
result=0
cnt=0
for i in arr:
    cnt+=1
    if cnt >= i:
        result+=1
        cnt=0
print(cnt)