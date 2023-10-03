from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    distance = [-1] * (n+1)
    graph = [[] for _ in range(n+1)]
    for to, fr in roads:
        graph[to].append(fr)
        graph[fr].append(to)
    q=deque([destination])
    distance[destination]=0
    while q:
        now = q.popleft()
        for pre in graph[now]:
            if distance[pre]==-1:
                q.append(pre)
                distance[pre]=distance[now]+1
    for source in sources:
        answer.append(distance[source])
    return answer