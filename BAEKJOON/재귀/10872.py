# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)

a=int(input())
print(fac(a))


# 예제 입력 1 
# 10
# 예제 출력 1 
# 3628800
# 예제 입력 2 
# 0
# 예제 출력 2 
# 1