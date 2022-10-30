ssum = 0
mink = 21e8
N=int(input())
M=int(input())
arr=[True] * (M+1)

for i in range(2, M+1):
    if arr[i] == False: continue
    for j in range(i+i, M+1,i):
        arr[j] = False
arr[0]=False
arr[1]=False
for k in range(N, M+1):
    if arr[k]==True:
        ssum += k
        if mink > k:
            mink = k
if mink == 21e8:
    mink = -1
if ssum != 0:
    print(ssum)
print(mink)

