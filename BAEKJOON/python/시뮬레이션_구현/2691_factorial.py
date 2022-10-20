T=int(input())
arr=list(map(int, input().split()))
max_re=1
cnt=1
arr_1=arr[::-1]

for i in range(1,T):
    if arr[i]>=arr[i-1]:
        cnt += 1
        if cnt > max_re:
            max_re = cnt
    else:
        cnt=1
cnt=1
for i in range(1,T):
    if arr_1[i]>=arr_1[i-1]:
        cnt += 1
        if cnt > max_re:
            max_re = cnt
    else:
        cnt=1

print(max_re)

