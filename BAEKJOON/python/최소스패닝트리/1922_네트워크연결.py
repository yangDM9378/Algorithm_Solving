n=int(input())
e=int(input())
edges=[]
parent=[0]*(n+1)
result =0
def find_parent(parent,a):
    if parent[a] != a:
        parent[a]=find_parent(parent,parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

for i in range(n+1):
    parent[i]=i

for _ in range(e):
    a,b,cost = map(int, input().split())
    edges.append((cost,a,b))
edges.sort()

for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent, a, b)
        result+= cost

print(result)