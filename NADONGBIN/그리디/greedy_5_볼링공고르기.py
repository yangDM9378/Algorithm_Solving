"""
입력 예시
5 3
1 3 2 3 2

입력예시
8 5
1 5 4 3 2 4 5 2
"""

n,m = map(int, input().split())
arr=list(map(int, input().split()))

cnt = [0]*11

for data in arr:
    cnt[data]+=1
result=0
for i in range(1,m+1):
    n-=cnt[i]
    result += cnt[i]*n
print(result)