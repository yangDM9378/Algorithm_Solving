# 평균값 구하기
# 10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
# (소수점 첫째 자리에서 반올림한 정수를 출력한다.)

T = int(input())
for test_case in range(1, T + 1):
    a = list(map(int, input().split()))
    b=round(sum(a)/len(a))
    print('#%d %d' %(test_case, b))

# 입력
# 3
# 3 17 1 39 8 41 2 32 99 2
# 22 8 5 123 7 2 63 7 3 46
# 6 63 2 3 58 76 21 33 8 1  

# 출력
# #1 24
# #2 29
# #3 27