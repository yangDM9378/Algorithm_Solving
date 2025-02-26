def GCD(a,b):
    while True:
        if a % b == 0:
            return b
        tmp = a % b
        a = b
        b = tmp

def solution(arr):
    answer = 0
    sort_arr = sorted(arr)
    a = sort_arr.pop()
    while sort_arr:
        b = sort_arr.pop()
        tmp = a * b
        a = tmp / GCD(a,b)
    return a 