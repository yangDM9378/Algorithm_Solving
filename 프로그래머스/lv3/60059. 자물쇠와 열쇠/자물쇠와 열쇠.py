from copy import deepcopy
def keyRotation(key_rotations):
    n=len(key_rotations[0])
    arr=[[0]*n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            arr[y][x] = key_rotations[-1][n-1-x][y]
    key_rotations.append(arr)
    
def key_push(arr_copy,n,m,start_y,start_x,key_rotation):
    for y in range(n):
        for x in range(n):
            # if key_rotation[y][x]==1 and arr_copy[start_y+y][start_x+x]==0:
            #     arr_copy[start_y+y][start_x+x]==1
            arr_copy[start_y+y][start_x+x]+=key_rotation[y][x]
    return arr_copy
def check_arr(arr_copy,n,m):
    for y in range(n-1, n+m-1):
        for x in range(n-1,n+m-1):
            if arr_copy[y][x] != 1:
                return False
    return True
    
def solution(key, lock):
    answer = True
    n=len(key)
    m=len(lock)
    key_rotations = []    
    key_rotations.append(key)
    for _ in range(3):
        keyRotation(key_rotations)
    arr=[[0]*(m+2*(n-1)) for _ in range(m+2*(n-1))]
    for y in range(m):
        for x in range(m):
            arr[n-1+y][n-1+x]=lock[y][x]
    for key_rotation in key_rotations:
        for start_y in range(m+n-1):
            for start_x in range(m+n-1):
                arr_copy=deepcopy(arr)
                arr_copy = key_push(arr_copy,n,m,start_y,start_x,key_rotation)
                result = check_arr(arr_copy,n,m)
                if result:
                    return result
    return False