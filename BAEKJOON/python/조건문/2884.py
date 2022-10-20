a = list(map(int, input().split()))
if a[0]<24 and a[0]!=0:
    if a[1]-45<0:
        k1=a[0]-1
        k2=60+(a[1]-45)
        print(k1,k2)
    else:
        k1=a[0]
        k2=a[1]-45
        print(k1,k2)
elif a[0]==0:
    if a[1]-45<0:
        k1=23
        k2=60+(a[1]-45)
        print(k1,k2)
    else:
        k1=a[0]
        k2=a[1]-45
        print(k1,k2)
else:
    if a[1]-45<0:
        k1=23
        k2=60+(a[1]-45)
        print(k1,k2)
    else:
        k1=a[0]
        k2=a[1]-45
        print(k1,k2)