# 위 표에서 C보다 더 큰 덩치의 사람이 없으므로 C는 1등이 된다. 그리고 A, B, D 각각의 덩치보다 큰 사람은 C뿐이므로 이들은 모두 2등이 된다. 그리고 E보다 큰 덩치는 A, B, C, D 이렇게 4명이므로 E의 덩치는 5등이 된다. 위 경우에 3등과 4등은 존재하지 않는다. 여러분은 학생 N명의 몸무게와 키가 담긴 입력을 읽어서 각 사람의 덩치 등수를 계산하여 출력해야 한다.

T=int(input())
li=[]
for _ in range(T):
    li.append(list(map(int, input().split())))
for i in range(T):
    a=1
    for j in range(T):
        if (li[i][0]<li[j][0]) and (li[i][1]<li[j][1]):
            a+=1    
    print(a, end=' ')


# 예제 입력 1 
# 5
# 55 185
# 58 183
# 88 186
# 60 175
# 46 155
# 예제 출력 1 
# 2 2 1 2 5