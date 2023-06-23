"""
입력 예시
5 3
1 2 5 4 3
5 5 6 6 5
"""

n,k = map(int, input().split())
a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

a_arr = sorted(a_arr)
b_arr = sorted(b_arr)

for i in range(k):
    if a_arr[i] < b_arr[i]:
        a_arr[i],b_arr[i]= b_arr[i], a_arr[i]
    else:
        break

print(sum(a_arr))