N, D = map(int, input().split())
arr = [i for i in range(D+1)]
graph = [list(map(int, input().split())) for _ in range(N)]
for i in range(D+1):
    arr[i] = min(arr[i], arr[i-1]+1)
    for s, e, d in graph:
        if i == s and e <= D and arr[i]+d < arr[e]:
            arr[e]=arr[i]+d
print(arr[D])
