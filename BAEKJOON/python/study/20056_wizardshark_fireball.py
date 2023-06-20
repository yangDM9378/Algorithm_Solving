N,M,K= map(int, input().split())

arr = list([[] for _ in range(N)] for _ in range(N))
print(arr)
magic=[]
for _ in range(M):
    r,c,m,s,d = map(int, input().split())
    arr[r-1][c-1].append([m,s,d])
direct_fireball = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
for _ in range(K):
