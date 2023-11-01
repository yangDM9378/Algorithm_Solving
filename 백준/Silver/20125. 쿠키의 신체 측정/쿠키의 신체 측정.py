# 머리 위치 찾기
def head_idx(arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '*':
                return i,j

def dhls_hand(y,x):
    cnt = 0
    for i in range(x-1,-1,-1):
        cnt+=1
        if arr[y][i] =='_':
            return cnt-1
    return cnt

def dh_hand(y,x):
    cnt = 0
    for i in range(x+1,n,1):
        cnt+=1
        if arr[y][i] =='_':
            return cnt-1
    return cnt

def waist(y,x):
    cnt=0
    for i in range(y,n):
        cnt+=1
        if arr[i][x] =='_':
            break
    return cnt-1

def leg(y,x):
    cnt=1
    for i in range(y,n):
        if arr[i][x] == '_':
            break
        cnt += 1
    return cnt - 1

n=int(input())
arr=[]
for _ in range(n):
    row = input()
    arr.append(list(row))

y,x = head_idx(arr)
print(y+2,x+1)
print(dhls_hand(y+1,x), end=' ')
print(dh_hand(y+1,x), end=' ')
waist_cnt = waist(y+2,x)
print(waist_cnt, end=' ')
print(leg(y+waist_cnt+2,x-1), end=' ')
print(leg(y+waist_cnt+2,x+1), end=' ')
