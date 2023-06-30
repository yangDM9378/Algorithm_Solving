"""
입력 예시
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
"""

def find_parent(parents,a):
    if parents[a] != a:
        parents[a] = find_parent(parents,parents[a])
    return parents[a]

def union_parent(parents,a,b):
    a=find_parent(parents,a)
    b=find_parent(parents,b)
    if a<b :
        parents[b]=a
    else:
        parents[a]=b


v,e= map(int, input().split())
parents = [0]*(v+1)

edges =[]
result = 0

for i in range(1, v+1):
    parents[i]=i

for _ in range(e):
    a,b,cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parents,a) != find_parent(parents,b):
        union_parent(parents, a,b)
        result += cost

print(result)