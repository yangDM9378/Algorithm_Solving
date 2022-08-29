# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

li=[]
for i in range(9):
    k=int(input())
    li.append(k)
print(max(li))
print(li.index(max(li))+1)

# 예제 입력 1 
# 3
# 29
# 38
# 12
# 57
# 74
# 40
# 85
# 61
# 예제 출력 1
# 85
# 8