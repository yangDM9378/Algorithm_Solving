"""
입력예시
2
홍길동 95
이순신 77
"""

n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(str, input().split())))

arr=sorted(arr, key=lambda x:int(x[1]))

for a in arr:
    print(a[0], end=' ')