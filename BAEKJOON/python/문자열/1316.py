# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

T=int(input())
re=0
for i in range(T):
    words=input()
    li=[]
    li.append(words[0])
    for i in range(1,len(words)):
        if words[i]!=words[i-1]:
            li.append(words[i])
    if len(set(li))==len(li):
        re+=1
print(re)

# 예제 입력 1 
# 3
# happy
# new
# year
# 예제 출력 1 
# 3
# 예제 입력 2 
# 4
# aba
# abab
# abcabc
# a
# 예제 출력 2 
# 1
# 예제 입력 3 
# 5
# ab
# aa
# aca
# ba
# bb
# 예제 출력 3 
# 4
# 예제 입력 4 
# 2
# yzyzy
# zyzyz
# 예제 출력 4 
# 0
# 예제 입력 5 
# 1
# z
# 예제 출력 5 
# 1
