# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
while True:
    a,b = map(int, input().split())
    if a==0 and b==0:
        break
    else:
        print(a+b)

# 예제 입력 1
# 1 1
# 2 3
# 3 4
# 9 8
# 5 2
# 0 0

# 예제 출력 1
# 2
# 5
# 7
# 17
# 7