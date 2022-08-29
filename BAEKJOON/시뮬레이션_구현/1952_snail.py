a,b =map(int,input().split())
arr=[[0]*b for _ in range(a)]

diry=[0,1,0,-1]
dirx=[1,0,-1,0]
y=0
x=0
n=1
i=0
arr[0][0]=3
while n<=a*b:
    y=diry[i]+y
    x=dirx[i]+x
    if y<0 or y>a-1 or x<0 or x>b-1 or arr[y][x]!=0:
        y=y-diry[i]
        x=x-dirx[i]
        arr[y][x] = 1
        i=(i+1)%4
        y=y+diry[i]
        x=x+dirx[i]
        arr[y][x] = 3

    n+=1
cnt=0
for i in range(a):
    for j in range(b):
        if arr[i][j]==1:
            cnt+=1
if cnt<0:
    print(0)
else:
    print(cnt-1)

