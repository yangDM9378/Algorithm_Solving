
T=int(input())
for t in range(T):
    N,M=map(int, input().split())
    queue=list(map(int, input().split()))
    for _ in range(M):
        queue.append(queue.pop(0))
    print(f'#{t+1} {queue.pop(0)}')