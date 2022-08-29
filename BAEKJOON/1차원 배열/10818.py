# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

T=int(input())
k=list(map(int, input().split()))
max_li=max(k)
min_li=min(k)
print(f'{min_li} {max_li}')

# 예제 입력 1
# 5
# 20 10 35 30 7
# 예제 출력 1
# 7 35