n=int(input())
arr=list(map(int, input().split()))
m=int(input())
start, end = 0, max(arr)

while True:
    if start > end:
        break
    mid = (start+end)//2
    total = 0
    for i in arr:
        if i <= mid:
            total += i
        else:
            total += mid
    if total <= m:
        start=mid+1
    else:
        end = mid-1
print(end)