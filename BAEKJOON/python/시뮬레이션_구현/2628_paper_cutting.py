a,b=map(int, input().split())
T=int(input())
li_0=[]
li_1=[]
li_0.append(0)
li_1.append(0)
li_0.append(b)
li_1.append(a)
for _ in range(T):
    c,d=map(int, input().split())
    if c==0:
        li_0.append(d)
    else:
        li_1.append(d)
li_0.sort()
li_1.sort()

re_0=[]
re_1=[]
for i in range(1,len(li_0)):
    re_0.append(li_0[i]-li_0[i-1])
for i in range(1,len(li_1)):
    re_1.append(li_1[i]-li_1[i-1])

result=0
for i in range(len(re_0)):
    for j in range(len(re_1)):
        if result<(re_0[i]*re_1[j]):
            result=(re_0[i]*re_1[j])
print(result)

