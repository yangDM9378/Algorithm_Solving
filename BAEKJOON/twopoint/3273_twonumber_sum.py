
# # 시간복잡도 O(n^2) 시간초과
# n=int(input())
# arr=list(map(int, input().split()))
# x=int(input())
# cnt=0
# for i in range(n-1):
#     for j in range(i+1,n):
#         if arr[i]+arr[j] == x:
#             cnt+=1
# print(cnt)


n=int(input())
arr=list(map(int, input().split()))
x=int(input())
arr.sort()
s=0
e=n-1
cnt=0
while s<e:
    if x==arr[s]+arr[e]:
        e=e-1
        cnt+=1
    elif x>arr[s]+arr[e]:
        s=s+1
    else:
        e=e-1
print(cnt)