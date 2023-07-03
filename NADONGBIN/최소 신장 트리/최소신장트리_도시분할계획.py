"""
입력예시
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
"""

def find_parent(parents,a):
    if parents[a] != a:
        parents[a] = find_parent(parents, parents[a])
    return parents[a]

def union_parent(parents,a,b):
    a=find_parent(parents,a)
    b=find_parent(parents,b)
    if a<b:
        parents[b]=a
    else:
        parents[a]=b
v,e =  map(int, input().split())
parents = [0]*(v+1)
edges=[]
result =0

for i in range(1, v+1):
    parents[i]=i

for _ in range(e):
    a,b,cost = map(int, input().split())
    edges.append((cost, a,b))

edges.sort()
last = 0

for edge in edges:
    cost,a,b = edge
    if find_parent(parents,a) != find_parent(parents,b):
        union_parent(parents,a,b)
        result += cost
        last = cost

print(result - last)