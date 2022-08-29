for t in range(10):
    N=int(input())
    arr=list(map(int, input().split()))
    for i in range(N):
        a=max(arr)
        b=min(arr)
        max_x = arr.index(a)
        min_x = arr.index(b)
        min_index=min_x
        max_index=max_x
        arr[min_index]+=1
        arr[max_index]-=1
    print(f'#{t+1} {max(arr)-min(arr)}')

