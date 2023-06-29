"""
입력예시
6 4
1 4
2 3
2 4
5 6
"""

def find_parent(parent,a):
    if parent[a] != a:
        parent[a]= find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v, e= map(int, input().split())
parent = [0]*(v+1)

# 부모랑 나랑 같게 하기
for i in range(1,v+1):
    parent[i]=i

for i in range(e):
    a,b = map(int, input().split())
    union_parent(parent, a, b)

for i in range(1, v+1):
    print(find_parent(parent,i), end=' ')
print()

for i in range(1, v+1):
    print(parent[i], end=' ')