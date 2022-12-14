# 상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
# 상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.
# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

N=int(input())
k=0

while N>=0:
    # 최소의 봉지를 구하는 것은 5가 큰수 이기 때문에 5로 나누어 떨어질때 갯수를 구하면 됨
    # +5로 나누어 떨어지지 않지만 3씩 빼며 봉지 개수를 증가 시켜 3kg과 5kg 무게 확인
    if N%5==0:
        k=k+N//5
        print(k)
        break
    else:
        N-=3
        k+=1

# N을 3씩 빼고 5로 나누어 떨어지지 않아 -1또는 -2가 되면 -1 출력
if N<0:
    print(-1)


# 예제 입력 1 
# 18
# 예제 출력 1 
# 4
# 예제 입력 2 
# 4
# 예제 출력 2 
# -1
# 예제 입력 3 
# 6
# 예제 출력 3 
# 2
# 예제 입력 4 
# 9
# 예제 출력 4 
# 3
# 예제 입력 5 
# 11
# 예제 출력 5 
# 3