"""
입력예시
4 4 2 1
1 2
1 3
2 3
2 4

입력예시
4 3 2 1
1 2
1 3
1 4

입력예시
4 4 1 1
1 2
1 3
2 3
2 4
"""

n,m,k,x=map(int, input().split())
arr=[[] for _ in range(n+1)]

for _ in range(m):
    start,end = map(int, input().split())
    arr[start].append(end)
check = [999999]*(n+1)
def dfs(go,level):
    global result, check
    if level > k:
        return
    if check[go]>level:
        check[go]=level
    for next in arr[go]:
        dfs(next, level+1)
check[x]=0
dfs(x,0)
result =[]

for i in range(len(check)):
    if check[i]==k:
        result.append(i)
if len(result)==0:
    print(-1)
else:
    for i in result:
        print(i)