def find(member): #부모찾기
    global z
    if z[member]==member:
        return member
    ret=find(z[member])
    z[member]=ret
    return ret

def union(a,b):
    global z
    fa,fb=find(a),find(b)
    if fa==fb: return True
    z[fb]=fa

N=int(input())
M=int(input())
li=[]
arr=[list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i>j and arr[i][j]==1:
            li.append([i,j])
z=[i for i in range(N)]
for lst in li:
    a,b=lst
    union(a,b)

result=list(map(int, input().split()))
temp=find(z[result[0]-1])
ret=-1
for i in range(1,len(result)):
    if find(z[result[i]-1])==temp:
        temp=find(z[result[i]-1])
    else:
        ret=0
        break
if ret==0:
    print('NO')
else:
    print('YES')