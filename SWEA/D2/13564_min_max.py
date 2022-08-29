import sys
sys.stdin=open("TEST.txt","r")

T=int(input())
for k in range(T):
    a=int(input())
    arr=list(map(int, input().split()))
    max_arr=arr[0]
    min_arr=arr[0]
    for i in range(1,a):
        if max_arr<arr[i]:
            max_arr=arr[i]
    for j in range(1,a):
        if min_arr>arr[j]:
            min_arr=arr[j]
    print(f'#{k+1} {max_arr-min_arr}')
