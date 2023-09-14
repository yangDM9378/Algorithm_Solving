def solution(a):
    arr=[False]*len(a)
    min_l=21e8
    min_r=21e8
    for i in range(len(a)):
        if a[i]<min_l:
            min_l = a[i]
            arr[i]=True
        if a[-1-i]<min_r:
            min_r = a[-1-i]
            arr[-1-i]=True
    return sum(arr)