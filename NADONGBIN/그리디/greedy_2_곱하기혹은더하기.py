"""
입력예시
02984

입력예시
567
"""
arr=list(input())
result = int(arr[0])
for i in range(1,len(arr)):
    if int(arr[i]) <= 1 or result <= 1 :
        result += int(arr[i])
    else:
        result *= int(arr[i])
print(result)