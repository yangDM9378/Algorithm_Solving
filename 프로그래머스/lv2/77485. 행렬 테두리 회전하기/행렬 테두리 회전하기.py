def solution(rows, columns, queries):
    answer = []
    arr=[[0]*columns for _ in range(rows)]
    for i in range(1,rows+1):
        for j in range(1, columns+1):
            arr[i-1][j-1]=((i-1) * columns + j)
    for query in queries:
        min_value = 21e8
        x1,y1,x2,y2 = query[0]-1,query[1]-1,query[2]-1,query[3]-1
        temp=arr[x1][y1]
        print(x1,y1,x2,y2)
        for i in range(x1,x2):
            arr[i][y1]=arr[i+1][y1]
            min_value = min(min_value,arr[i+1][y1])
        for i in range(y1,y2):
            arr[x2][i]=arr[x2][i+1]
            min_value = min(min_value, arr[x2][i+1])
        for i in range(x2,x1,-1):
            arr[i][y2]=arr[i-1][y2]
            min_value = min(min_value, arr[i-1][y2])
        for i in range(y2,y1+1,-1):
            arr[x1][i]=arr[x1][i-1]
            min_value = min(min_value, arr[x1][i-1])
        arr[x1][y1+1] =temp
        answer.append(min(min_value, temp))
    return answer