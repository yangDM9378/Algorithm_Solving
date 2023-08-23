import math
def solution(n, k):
    answer=[]
    arr=[i for i in range(1,n+1)]
    while True:
        n=n-1
        if len(arr)==0:
            break
        di, k = divmod(k, math.factorial(n))
        if k==0:
            answer.append(arr[di-1])
            arr.remove(arr[di-1])
        else:
            answer.append(arr[di])
            arr.remove(arr[di])
    return answer