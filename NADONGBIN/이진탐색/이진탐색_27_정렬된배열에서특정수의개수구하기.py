"""
입력예시1
7 2
1 1 2 2 2 2 3

입력예시2
7 4
1 1 2 2 2 2 3

입력예시3
20 2
1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
"""

n,x = map(int, input().split())
arr = list(map(int, input().split()))

start=0
end = n-1
cnt=0
def binary(start,end):
    global cnt
    while start <= end:
        mid = (start+end) //2
        if arr[mid]== x:
            cnt+=1
            binary(start,mid-1)
            binary(mid+1,end)
            return
        if arr[mid] > x:
            end=mid-1
        elif arr[mid] < x:
            start=mid+1

binary(start, end)
if cnt == 0:
    print(-1)
else:
    print(cnt)