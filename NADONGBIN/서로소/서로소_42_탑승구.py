"""
입력예시
4
3
4
1
1

입력예시
4
6
2
2
3
3
4
4
"""
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,x,y):
    x=find_parent(parent,x)
    y=find_parent(parent,y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y

g=int(input())
p=int(input())
parent=[0]*(g+1)
result = 0
parent=[0]*(g+1)
for i in range(1, g+1):
    parent[i]=i
for i in range(p):
    data = find_parent(parent, int(input()))
    if data ==0:
        break
    union_parent(parent,data,data-1)
    result+=1
print(result)