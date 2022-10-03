def find(member):
    global arr
    if arr[member]==member:
        return member
    ret=find(arr[member])
    arr[member]=ret
    return ret

def union(a,b):
    global arr
    global result
    a, b=find(a),find(b)
    if a==b: return False
    arr[b]=a
    return True

V,E=map(int, input().split())
li=[]
arr=[i for i in range(V+1)]
for _ in range(E):
    a,b,c=map(int, input().split())
    li.append((c,a,b))
li.sort()
cnt=0
result=0
for lst in li:
    c,a,b=lst
    if a>b:
        a,b=b,a
    if union(a,b):
        cnt+=c
print(cnt)