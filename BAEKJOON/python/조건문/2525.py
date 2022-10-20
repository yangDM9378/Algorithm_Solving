a,b = map(int, input().split())
c=int(input())
if (b+c)//60==0:
    a=a%24
    b=b+c
else:
    a=(a+(b+c)//60)%24
    b=(b+c)%60
print(a,b)