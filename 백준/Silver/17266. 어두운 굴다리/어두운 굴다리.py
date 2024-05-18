import math
n=int(input())
M=int(input())
x = list(map(int,input().split()))
height = 0
for i in range(1,len(x)):
    height = max(math.ceil((x[i]-x[i-1])/2), height)
print(max(height,x[0],n-x[-1]))
