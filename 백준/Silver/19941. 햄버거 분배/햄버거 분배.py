n,k = map(int, input().split())
arr = list(input())

def eat_cnt(start,end):
    for i in range(start, end+1):
        if arr[i]=='H':
            arr[i]='X'
            return 1
    return 0

cnt = 0
for i in range(len(arr)):
    if arr[i]=='P':
        start = i-k
        end = i+k
        if start<0:
            start = 0
        if end > len(arr)-1:
            end = len(arr)-1
        cnt += eat_cnt(start,end)
print(cnt)