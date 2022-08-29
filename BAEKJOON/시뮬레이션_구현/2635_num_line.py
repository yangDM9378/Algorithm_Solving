n=int(input())
result=[]
for i in range(1,n+1):
    li = []
    li.append(n)
    li.append(i)
    while 1:
        if li[-2]-li[-1]<0:
            break
        else:
            li.append(li[-2]-li[-1])
    result.append(li)

a=sorted(result, key=lambda x:-len(x))
print(len(a[0]))
print(*a[0])






