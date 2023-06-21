"""
입력 예시
5
R R R U D D
"""

N = int(input())
arr = list(map(str, input().split()))

y=0
x=0
go_arr = [[0,-1],[0,1],[-1,0],[1,0]]
for go in arr:
    if go =='L':
        dy = y+go_arr[0][0]
        dx = x+go_arr[0][1]
        if 0 <= dy < N and 0 <= dx < N:
            y,x=dy,dx
    elif go == 'R':
        dy = y+go_arr[1][0]
        dx = x+go_arr[1][1]
        if 0 <= dy < N and 0 <= dx < N:
            y,x=dy,dx

    elif go == 'U':
        dy = y+go_arr[2][0]
        dx = x+go_arr[2][1]
        if 0 <= dy < N and 0 <= dx < N:
            y,x=dy,dx
    else:
        dy = y+go_arr[3][0]
        dx = x+go_arr[3][1]
        if 0 <= dy < N and 0 <= dx < N:
            y,x=dy,dx
print(y+1,x+1)

# 코드 간결화
N = int(input())
arr = list(map(str, input().split()))
y,x=1,1
diry=[0,0,-1,1]
dirx=[-1,1,0,0]
move_types = ['L','R','U','D']
for go in arr:
    for i in range(len(move_types)):
        if go == move_types[i]:
            dy = y + diry[i]
            dx = x + dirx[i]
        if 0 <= dy < N and 0 <= dx < N:
            y,x = dy,dx
print(y,x)