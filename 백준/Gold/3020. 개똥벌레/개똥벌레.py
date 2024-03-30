import sys
N,H = map(int, input().split())
up = [0]*(H+1)
down = [0]*(H+1)
for i in range(N):
    num = int(input())
    if i%2 == 0:
        up[num] += 1
    else:
        down[num]+=1

for i in range(H,0,-1):
    up[i-1]=up[i]+up[i-1]
    down[i-1] = down[i] + down[i-1]
for i in range(H):
    up[i+1]=up[i+1]+down[H-i]
print(min(up[1::]), up[1::].count(min(up[1::])))