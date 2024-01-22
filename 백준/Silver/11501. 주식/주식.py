T=int(input())

for _ in range(T):
    n=int(input())
    arr = list(map(int, input().split()))
    result = 0
    max_price = 0
    for i in range(len(arr)-1,-1,-1):
        if arr[i] > max_price:
            max_price = arr[i]
        else:
            result += max_price - arr[i]
    print(result)