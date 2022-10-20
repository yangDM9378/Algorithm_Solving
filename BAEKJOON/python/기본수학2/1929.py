# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# a,b =map(int, input().split())

# 루트로 계산 -> 에라토스테네스 체
# 예전에 푼적있음....
for i in range(a,b+1):
    if i==1:
        continue
    # 제곱근까지만 확인하면 됨
    for j in range(2, int(i**1/2)+1):
        if i%j==0:
            break
    
    else:
        print(i)


# 예제 입력 1 
# 3 16
# 예제 출력 1 
# 3
# 5
# 7
# 11
# 13