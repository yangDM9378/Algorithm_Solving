"""
입력예시
0001100
"""

arr=list(input())
cnt_0=0
cnt_1=0

if arr[0]=='1':
    cnt_0 += 1
else:
    cnt_1 += 1

for i in range(len(arr)-1):
    if arr[i] != arr[i-1]:
        if arr[i+1] =='1':
            cnt_0+=1
        else:
            cnt_1+=1

print(max(cnt_1,cnt_0))