"""
입력예시
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
"""
def union_parent(parents,a):
    if parents[a]!=a:
        parents[a]=union_parent(parents,parents[a])
    return parents[a]

def find_parents(parents,i,j):
    i=union_parent(parents,i)
    j=union_parent(parents,j)
    if i<j:
        parents[j]=i
    else:
        parents[i]=j


city_num, tour_num= map(int, input().split())

parents = [0]*(city_num+1)

for i in range(city_num+1):
    parents[i]=i

for i in range(city_num):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        if line[j]==1:
            find_parents(parents,i+1,j+1)

checks = list(map(int, input().split()))
result = 0
for check in checks:
    if parents[check] != parents[checks[1]]:
        result = 1
if result == 0:
    print('YES')
else:
    print('NO')