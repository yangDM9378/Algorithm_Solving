T=int(input())
arr = []
for _ in range(T):
    lh = list(map(int,input().split()))
    arr.append(lh)
arr.sort(key=lambda x:x[0])
ssum = 0
idx = 0
l,h = arr[0]
for i in range(1,len(arr)):
    if arr[i][1] >= h:
        cal = (arr[i][0]-l)*h
        ssum+=cal
        idx = i
        l,h = arr[i]
ssum+=h
l,h = arr[-1]
for i in range(len(arr)-1,idx-1,-1):
    if arr[i][1] >= h:
        cal = (l-arr[i][0])*h
        ssum+=cal
        idx = i
        l,h = arr[i]
print(ssum)