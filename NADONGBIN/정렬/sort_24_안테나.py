"""
입력 예시
4
5 1 7 9
"""

n=int(input())
arr=list(map(int, input().split()))
arr.sort()
print(arr[(n-1)//2])