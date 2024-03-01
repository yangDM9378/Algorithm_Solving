N, d, k, c = map(int, input().split())
plate = []

for _ in range(N):
    plate.append(int(input()))

check = [0] * (d + 1)
distinct_count = 0
max_cnt = 0

for i in range(k):
    if check[plate[i]] == 0:
        distinct_count += 1
    check[plate[i]] += 1

if check[c] == 0:
    distinct_count += 1
check[c] += 1
max_cnt = distinct_count

for i in range(1, N):
    if check[plate[i - 1]] == 1:
        distinct_count -= 1
    check[plate[i - 1]] -= 1

    if check[plate[(i + k - 1) % N]] == 0:
        distinct_count += 1
    check[plate[(i + k - 1) % N]] += 1

    if check[c] == 0:
        distinct_count += 1
    max_cnt = max(max_cnt, distinct_count)

print(max_cnt)
