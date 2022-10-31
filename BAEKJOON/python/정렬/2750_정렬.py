n=int(input())
li = []
for _ in range(n):
    k = int(input())
    li.append(k)
li.sort()
for i in range(n):
    print(li[i])