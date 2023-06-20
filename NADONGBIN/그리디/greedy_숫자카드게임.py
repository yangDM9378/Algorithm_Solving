"""
입력예제 1
3 3
3 1 2
4 1 4
2 2 2

입력 예제 2
2 4
7 3 1 8
3 3 3 4
"""

# 행별로 가장 작은 값중 제일 큰값을 찾으면 되는 문제
N,M = map(int, input().split())
result = 0
for i in range(N):
    values = list(map(int, input().split()))
    min_value = min(values)
    max_min_value = max(result, min_value)
print(max_min_value)