def find(a):
    global li
    if li[a]==a:
        return a
    ret=find(li[a])
    li[a]=ret
    return ret

def union(a,b):
    global li
    a,b=find(a),find(b)
    if a==b:return False
    li[b]=a
    return True

n=int(input())
li=[]
for _ in range(n):
    x,y=map(float,input().split())
    li.append((x,y))
arr=[]
for i in range(n-1):
    for j in range(i+1,n):
        dy=(li[i][0]-li[j][0])**2
        dx=(li[i][1]-li[j][1])**2
        direction=(dy+dx)**(1/2)
        arr.append((direction,i,j))
arr.sort()
li=[j for j in range(n)]
cnt=0
for i in arr:
    direction,a,b=i
    if union(a,b):
        cnt+=direction
print(round(cnt,2))
