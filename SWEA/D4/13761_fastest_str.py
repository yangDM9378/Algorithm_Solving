T=int(input())

for t in range(T):
    a, b = map(str, input().split())
    a=a.replace(b,'#')
    print(f'#{t+1} {len(a)}')
