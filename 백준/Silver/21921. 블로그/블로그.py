N,X = map(int,input().split())
arr=list(map(int, input().split()))
# 시작값
check_num = sum(arr[:X])
max_num = check_num
day = 1

for i in range(N-X):
    check_num=check_num-arr[i]+arr[i+X]
    if max_num == check_num:
        day+=1
    elif max_num < check_num:
        max_num = check_num
        day=1

if max_num == 0:
    print('SAD')
else:
    print(max_num)
    print(day)
