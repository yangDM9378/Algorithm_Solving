def find_parents(a,parents):
    if parents[a]!=a:
        parents[a]=find_parents(parents[a],parents)
    return parents[a]

def union_find(a,b,parents):
    a=find_parents(a,parents)
    b=find_parents(b,parents)
    if a>b:
        parents[a]=b
    else:
        parents[b]=a

def solution(n, costs):
    answer = 0
    used=[0]*n
    costs.sort(key=lambda x:(x[2],x[1]))
    parents = [i for i in range(n)]
    
    for a,b,cost in costs:
        if find_parents(a,parents)==find_parents(b,parents):continue
        union_find(a,b,parents)
        answer+=cost
    return answer