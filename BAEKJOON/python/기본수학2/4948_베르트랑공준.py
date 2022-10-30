while 1:
    n = int(input())
    cnt = 0
    if n == 0:
        break
    arr = [True] * (2*n+1)
    arr[0]=False
    arr[1]=False

    for i in range(2,2*n+1):
        if arr[i]==False:continue
        for j in range(i+i, 2*n+1, i):
            arr[j]=False
    for i in range(n+1, 2*n+1):
        if arr[i]==True:
            cnt+=1
    print(cnt)
