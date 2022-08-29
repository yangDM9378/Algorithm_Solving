# 큰 놈, 작은 놈, 같은 놈
# 2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.

a=int(input())
for i in range(1,a+1):
    b, c = map(int, input().split())
    if b>c:
        k='>'
    elif b<c:
        k='<'
    else:
        k='='
    print('#%d %s' %(i,k))

# 입력
# 3
# 3 8 
# 7 7 
# 369 123

# 출력
# #1 <
# #2 =
# #3 >

