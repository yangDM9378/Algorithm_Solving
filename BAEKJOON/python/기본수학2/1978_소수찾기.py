n = int(input())
arr = list(map(int,input().split()))
a = max(arr)+1
z = [True] * (a+1)
cnt = 0
for i in range(2, a+1):
    if z[i] == False: continue
    for j in range(i+i,a+1,i):
        z[j] = False
z[0]=False
z[1]=False
for j in arr:
    if z[j] == True:
        cnt+=1
print(cnt)