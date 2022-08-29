import math
N,K=map(int, input().split())
li_0=[0]*6
li_1=[0]*6
for _ in range(N):
    k=list(map(int, input().split()))
    if k[0]==1:
        li_0[k[1]-1]+=1
    else:
        li_1[k[1]-1]+=1
li=[]
for i in range(6):
    li.append(li_0[i])
    li.append(li_1[i])

cnt=0
for i in range(len(li)):
    cnt+=math.ceil(li[i]/K)
print(cnt)
