# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

T=int(input())
for i in range(T):
    k=input()
    li=[j for j in k]

    li_re=[]
    if li[0]=='O':
        li_re.append(1)
    else:
        li_re.append(0)

    for i in range(1,len(li)):
        if li[i]=='X':
            li_re.append(0)
        elif li[i]==li[i-1] and li[i-1]=='O':
            li_re.append(li_re[i-1]+1)
        else:
            li_re.append(1)

    print(sum(li_re))



# 예제 입력 1
# 5
# OOXXOXXOOO
# OOXXOOXXOO
# OXOXOXOXOXOXOX
# OOOOOOOOOO
# OOOOXOOOOXOOOOX
# 예제 출력 1
# 10
# 9
# 7
# 55
# 30