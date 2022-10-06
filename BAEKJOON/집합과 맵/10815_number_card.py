N=int(input())
arr=set(map(int, input().split()))
M=int(input())
arr_M=list(map(int, input().split()))
for i in arr_M:
    if i in arr:
        print(1, end=' ')
    else:
        print(0, end=' ')
