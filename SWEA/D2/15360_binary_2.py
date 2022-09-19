T=int(input())
for t in range(T):
    a=float(input())
    k=1
    n=0
    result=''
    while n<13:
        k/=2
        if a-k>=0:
            result+='1'
            a=a-k
            if a==0:
                break
        else:
            result+='0'
        n+=1
    if a!=0:
        result='overflow'
    print(f'#{t+1} {result}')