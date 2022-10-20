import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def find(member):
    if member ==arr[member]:
        return member
    arr[member]=find(arr[member])
    return arr[member]

def union(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return
    if a<b:
        arr[b]=a
    else:
        arr[a]=b

n,m=map(int, input().split())
arr=[i for i in range(n+1)]
for _ in range(m):
    k,a,b=map(int,input().split())
    if k==0:
        union(a,b)
    else:
        if find(a)==find(b):
            print('YES')
        else:
            print('NO')
