"""
입력예시
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""

def find_parent(parents, a):
    if parents[a] != a:
        parents[a]=find_parent(parents, parents[a])
    return parents[a]

def union_parent(parents,a,b):
    a = find_parent(parents,a)
    b = find_parent(parents,b)
    if a<b:
        parents[b] = a
    else:
        parents[a] = b

e, v = map(int, input().split())
parents = [0]*(e+1)

for i in range(len(parents)):
    parents[i] = i

for _ in range(v):
    check, a, b = map(int, input().split())
    if check == 0:
        union_parent(parents, a, b)
    else:
        if parents[a] == parents[b]:
            print('YES')
        else:
            print('NO')