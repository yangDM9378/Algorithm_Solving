T=int(input())
for t in range(T):
    print(f'#{t+1}')
    arr=[50000,10000,5000,1000,500,100,50,10]
    money=int(input())
    for i in range(8):
        if money-arr[i]>=0:
            print(money//arr[i], end=' ')
            money=money%arr[i]
        else:
            print(0, end=' ')
    print()
