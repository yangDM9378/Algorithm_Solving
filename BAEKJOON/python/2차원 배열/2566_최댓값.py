arr=[list(map(int,input().split())) for _ in range(9)]
k=-1
for i in range(9):
    for j in range(9):
        if k < arr[i][j]:
            k=arr[i][j]
            max_i=i
            max_j=j
print(k)
print(max_i+1,max_j+1)