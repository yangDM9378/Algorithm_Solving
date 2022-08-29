import sys
sys.stdin = open("GNS_test_input.txt", "r")

T=int(input())
dict={'ZRO':0, 'ONE':1,'TWO':2,'THR':3,'FOR':4,'FIV':5,'SIX':6,'SVN':7,'EGT':8,'NIN':9}
for t in range(T):
    a,b = map(str, input().split())
    print(a)
    arr=list(input().split())
    li=[]
    for i in range(int(b)):
        num_arr=dict[arr[i]]
        li.append(num_arr)
    li=sorted(li)
    for j in range(int(b)):
        li[j]=[k for k,v in dict.items() if v==li[j]].pop()

    for k in range(int(b)):
        print(li[k], end=' ')
