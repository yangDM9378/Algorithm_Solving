import sys
sys.stdin = open("input.txt", "r")

def last_2(arr):
    for i in range(100):
        if arr[99][i] == 2:
            return i

def direct(y,x):
    for i in range(3):
        arr[y][x]=3
        dy=y+diry[i]
        dx=x+dirx[i]
        if dy>=0 and dy<=99 and dx<=99 and dx>=0:
            if arr[dy][dx]==1:
                return dy,dx

diry=[0,0,-1]
dirx=[-1,1,0]
for t in range(10):
    T = int(input())
    arr=[list(map(int, input().split())) for _ in range(100)]
    x=0
    x=last_2(arr)
    y=99
    while 1:
        y,x=direct(y,x)
        if y==0:
            break
    print(f'#{T} {x}')



