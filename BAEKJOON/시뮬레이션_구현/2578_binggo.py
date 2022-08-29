def X(a):
    for y in range(5):
        for x in range(5):
            if arr[y][x]==a:
                arr[y][x]='X'
    return arr

def row_arr(arr):
    result=0
    for y in range(5):
        cnt=0
        for x in range(5):
            if arr[y][x]=='X':
                cnt+=1
        if cnt==5:
            result+=1
    return result

def col_arr(arr):
    result=0
    for x in range(5):
        cnt=0
        for y in range(5):
            if arr[y][x]=='X':
                cnt+=1
        if cnt==5:
            result+=1
    return result

def eorkr_1(arr):
    cnt=0
    for y in range(5):
        for x in range(5):
            if y==x and arr[y][x]=='X':
                cnt+=1
    if cnt==5:
        return 1
    else:
        return 0

def eorkr_2(arr):
    cnt=0
    for y in range(5):
        for x in range(5):
            if y+x==4 and arr[y][x]=='X':
                cnt+=1
    if cnt==5:
        return 1
    else:
        return 0

arr=[list(map(int, input().split())) for _ in range(5)]
social_arr=[list(map(int, input().split())) for _ in range(5)]
cnt=0
num=0
for i in range(5):
    for j in range(5):
        if num>=3:
            a=cnt
        else:
            cnt += 1
            a=social_arr[i][j]
            arr=X(a)
            num_row=row_arr(arr)
            num_col=col_arr(arr)
            num_eorkr_1=eorkr_1(arr)
            num_eorkr_2=eorkr_2(arr)
            num=num_row+num_col+num_eorkr_1+num_eorkr_2
print(a)





