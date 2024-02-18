check_arr = [0]*100001
s=0
e=0
n,k = map(int, input().split())
arr = list(map(int, input().split()))

max_len = 0
while True:
    if e == n:
        break
    if check_arr[arr[e]] == k:
        check_arr[arr[s]]-=1
        max_len = max(max_len, e-s)
        s += 1
    else:
        check_arr[arr[e]]+=1
        e += 1
    max_len = max(max_len, e - s)
print(max_len)