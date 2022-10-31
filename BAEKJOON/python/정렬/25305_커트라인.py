N, k = map(int, input().split())
li = list(map(int, input().split()))
li.sort(reverse=True)
print(li[k-1])