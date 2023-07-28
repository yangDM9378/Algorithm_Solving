import math
def dfs(level, numbers, make_num):
    global used,all_num
    if level !=0:
        all_num.add(int(make_num))

    if level == len(numbers):
        return
        
    for i in range(len(numbers)):
        if used[i]!=0:continue
        used[i]=1
        dfs(level+1, numbers, make_num+numbers[i])
        used[i]=0
        
        
def solution(numbers):
    global used, all_num
    all_num=set()
    used=[0]*len(numbers)
    dfs(0,numbers,'')
    max_num = max(all_num)
    print(all_num)
    primary_arr = [True for i in range(max_num+1)]
    primary_arr[0]=False
    primary_arr[1]=False
    for i in range(2, int(math.sqrt(max_num))+1):
        if primary_arr[i]==True:
            j=2
            while i*j <=max_num:
                primary_arr[i*j]=False
                j+=1
    answer = 0
    for num in all_num:
        if primary_arr[num] == True:
            answer+=1
    return answer