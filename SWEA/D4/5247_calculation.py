from collections import deque
def bfs(N,now):
    global arr
    q=deque()
    q.append([N,now])
    while q:
        node=q.popleft()
        cnt,now=node[0],node[1]

        if cnt==M:
            arr[cnt]=now
            break

        if 0<=cnt<=1000000 and arr[cnt]>now:
            arr[cnt]=now
            q.append([cnt+1,now+1])
            q.append([cnt-1,now+1])
            q.append([cnt*2,now+1])
            q.append([cnt-10,now+1])


T=int(input())
for t in range(T):
    N,M=map(int, input().split())
    arr=[21e8]*1000001
    bfs(N,0)
    print(f'#{t+1} {arr[M]}')


from collections import deque
def bfs(N):
    global arr
    q=deque()
    q.append(N)
    while q:
        cnt=q.popleft()
        now=arr[cnt]
        if cnt==M:
            break
        next_cnt=[cnt+1,cnt-1,cnt*2,cnt-10]
        for ncnt in next_cnt:
            if 0<ncnt<1000001 and arr[ncnt]>now+1:
                arr[ncnt]=now+1
                q.append(ncnt)
T=int(input())
for t in range(T):
    N,M=map(int, input().split())
    arr=[21e8]*1000001
    arr[N]=0
    bfs(N)
    print(f'#{t+1} {arr[M]}')


