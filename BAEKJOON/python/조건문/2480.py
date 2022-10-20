a = list(map(int, input().split()))
a=sorted(a)
if a[0]==a[1] and a[0]==a[2]:
    print(10000+max(a)*1000)
elif a[0]==a[1] or a[1]==a[2]:
    print(1000+a[1]*100)
else:
    print(max(a)*100)