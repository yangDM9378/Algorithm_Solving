"""
입력예시
5
3 2 1 1 9
"""
N=int(input())
arr=list(map(int, input().split()))
arr.sort()

target = 1
for x in arr:
    if target < x:
        break
    target+=x

print(target)