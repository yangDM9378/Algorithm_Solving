# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

T=int(input())
for i in range(T):
    a=list(map(int, input().split()))
    m_a=sum(a[1:])/a[0]
    li_k=[]
    for k in a[1:]:
        if k>m_a:
            li_k.append(k)
    print(f'{len(li_k)/len(a[1:])*100:.3f}%')

# 5
# 5 50 50 70 80 100
# 7 100 95 90 80 70 60 50
# 3 70 90 80
# 3 70 90 81
# 9 100 99 98 97 96 95 94 93 91