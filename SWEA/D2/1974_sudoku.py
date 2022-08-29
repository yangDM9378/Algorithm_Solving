def row_1(arr):
    for y in range(9):
        z = [0] * 9
        for x in range(9):
            z[arr[y][x]-1]=1
        if 0 in z:
            return 0

    return 1

def col_1(arr):
    for x in range(9):
        z = [0] * 9
        for y in range(9):
            z[arr[y][x]-1]=1
        if 0 in z:
            return 0
    return 1

def sq_1(arr):
    for i in range(3):
        z=[0]*9
        for y in range(3):
            for x in range(3):
                z[arr[i*3+y][i*3+x]-1]=1
        if 0 in z:
            return 0
    return 1

T=int(input())
for t in range(T):
    arr=[list(map(int, input().split())) for _ in range(9)]
    num_row=row_1(arr)
    num_col=col_1(arr)
    num_sq=sq_1(arr)
    num=num_row+num_col+num_sq
    if num==3:
        print(f'#{t+1} 1')
    else:
        print(f'#{t+1} 0')