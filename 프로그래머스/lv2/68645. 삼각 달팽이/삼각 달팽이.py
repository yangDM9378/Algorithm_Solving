def solution(n):
    answer = []
    arr = [[0]*i for i in range(1,n+1)]
    x=-1
    y=0
    num=1
    for i in range(n):
        for j in range(i,n):
            if i%3 == 0:
                x+=1
            elif i%3 ==1 :
                y+=1
            else:
                x-=1
                y-=1
            arr[x][y]=num
            num+=1
    for num_arr in arr:
        for num in num_arr:
            answer.append(num)
    return answer