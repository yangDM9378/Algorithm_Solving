arr=[0]*30
for _ in range(28):
    n=int(input())-1
    arr[n]=1
for i in range(30):
    if arr[i]==0:
        print(i+1)