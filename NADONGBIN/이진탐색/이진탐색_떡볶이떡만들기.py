"""
입력예시
4 6
19 15 10 17
"""

import sys
n,m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr = sorted(arr)
start = 0
end = arr[-1]
while True:
    mid = (start+end)//2
    result = 0
    for i in arr:
        cnt = i-mid
        if cnt > 0:
            result += cnt
    if result == m:
        print(mid)
        break
    elif result < m:
        end = mid-1
    else:
        start = mid+1

