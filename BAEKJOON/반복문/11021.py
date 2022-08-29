# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
T=int(input())
for i in range(T):
    a,b = map(int,input().split())
    print(f'Case #{i+1}: {a+b}')
    
# 예제 입력 1
# 5
# 1 1
# 2 3
# 3 4
# 9 8
# 5 2

# 예제 출력 1
# Case #1: 2
# Case #2: 5
# Case #3: 7
# Case #4: 17
# Case #5: 7