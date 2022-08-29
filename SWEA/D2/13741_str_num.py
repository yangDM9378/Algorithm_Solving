T=int(input())
for t in range(T):
    str1=list(input())
    str2=input()
    temp=0
    for i in str1:
        if temp<str2.count(i):
            temp=str2.count(i)
    print(f'#{t+1} {temp}')