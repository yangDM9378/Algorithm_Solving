# 자릿수 더하기
# 하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.

a = str(input())
i=0
for j in range(len(a)):
    i+=int(a[j])
print(i)

# 입력
# 6789

# 출력
# 30