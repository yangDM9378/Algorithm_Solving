# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

N,A=map(int, input().split())
X=list(map(int, input().split()))
for i in X:
    if i<A:
        print(i, end=' ')



# 예제 입력 1
# 10 5
# 1 10 4 9 2 3 8 5 7 6
# 예제 출력 1
# 1 4 2 3