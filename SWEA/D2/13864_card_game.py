# T=int(input())
# def kkk(k):
#     global li
#     if len(k)==1:
#         li.append(k.pop())
#         return
#     stack=[]
#     while k:
#         if len(k) % 2 == 0:
#             b = k.pop()
#             a = k.pop()
#             c = res(a, b)
#             stack.append(c)
#         else:
#             stack.append(k.pop())
#             b = k.pop()
#             a = k.pop()
#             c = res(a, b)
#             stack.append(c)
#
#     kkk(stack[::-1])
#
# def res(a,b):
#     temp=a[0]-b[0]
#     if temp==-1 or temp==2:
#         return b
#     return a
#
# for t in range(T):
#     N=int(input())
#     arr=list(map(int, input().split()))
#     arr_r=[]
#     arr_l=[]
#     li=[]
#     for i in range(1, (1+N)//2+1):
#         arr_l.append([arr[i-1],i])
#     for j in range((1+N)//2+1, N+1):
#         arr_r.append([arr[j-1],j])
#     print(arr_l)
#     print(arr_r)
#     kkk(arr_l)
#     kkk(arr_r)
#     b=li.pop()
#     a=li.pop()
#     result=res(a,b)
#     print(f'#{t+1} {result[1]}')

T=int(input())
def kkk(s,l):
    if s==l:
        return s
    a=kkk(s, (s+l)//2)
    b=kkk((s+l)//2+1,l)
    return res(a,b)
def res(a,b):
    temp=arr[a]-arr[b]
    if temp==-1 or temp==2:
        return b
    return a

for t in range(T):
    N=int(input())
    arr=list(map(int, input().split()))
    result=kkk(0,N-1)
    print(f'#{t+1} {result+1}')
