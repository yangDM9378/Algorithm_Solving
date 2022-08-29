# 몫과 나머지 출력하기
# 2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.

T=int(input())
for i in range(1,T+1):
    a, b=map(int, input().split())
    t=a//b
    y=a%b
    print(f'#{i} {t} {y}')


# 입력
# 3
# 9 2
# 15 6
# 369 15

# 출력
#1 4 1
#2 2 3
#3 24 9