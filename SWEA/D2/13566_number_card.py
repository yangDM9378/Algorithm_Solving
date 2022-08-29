T=int(input())
for i in range(T):
    a=int(input())
    arr=list(str(input()))
    z_li=[0]*10
    for j in range(len(arr)):
        z_li[int(arr[j])]+=1

    temp=0
    for k in range(len(z_li)):
        if z_li[k]>=temp:
            temp=z_li[k]
            maxk=k
    print(f'#{i+1} {maxk} {temp}')