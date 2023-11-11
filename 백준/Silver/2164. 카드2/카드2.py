from collections import deque

N = int(input())
q = deque([i for i in range(1, N + 1)])

while q:
    if len(q)==1:
        break
    q.popleft()
    move_num = q.popleft()
    q.append(move_num)

print(q[0])
