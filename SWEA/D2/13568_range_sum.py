T=int(input())


for i in range(T):

    def dyn(j):
        arr_sum=0
        for i in range(b):
            arr_sum+=arr[j + i]
        return arr_sum


    a,b=map(int, input().split())
    arr=list(map(int, input().split()))
    li=[]
    for j in range(a-b+1):
        li.append(dyn(j))

    print(f'#{i+1} {max(li)-min(li)}')
