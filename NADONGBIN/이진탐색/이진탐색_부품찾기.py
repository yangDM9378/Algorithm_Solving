"""
입력 예시
5
8 3 7 9 2
3
5 7 9
"""


import sys

def binary_search(target):
    start=0
    end= len(arr)-1
    while True:
        mid = (start+end) // 2
        if start > end:
            return 'no'
        if arr[mid] == target:
            return 'yes'
        if arr[mid] <= target:
            start = mid+1
        elif arr[mid] >= target:
            end = mid-1


n=int(input())
arr= list(map(int, sys.stdin.readline().rstrip().split()))
arr=sorted(arr)
m=int(input())
search_num = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(m):
    a=binary_search(search_num[i])
    print(a, end =' ')