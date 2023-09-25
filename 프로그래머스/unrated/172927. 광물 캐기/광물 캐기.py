def solution(picks, minerals):
    answer = 0
    point = {'diamond':25, 'iron':5 , 'stone':1}
    pick_sum=sum(picks)
    minerals_sum = len(minerals)
    check_mineral_cnt = min(pick_sum*5,minerals_sum)
    check_mineral_dic = {}
    cnt=0
    arr= [[1,1,1],[5,1,1],[25,5,1]]
    for i in range(check_mineral_cnt):
        cnt+=1
        if cnt==5:
            cnt=0
        check_mineral_dic[i//5]=check_mineral_dic.get(i//5,0)
        check_mineral_dic[i//5]+=point[minerals[i]]
    check_mineral_dic = sorted(check_mineral_dic.items(), reverse=True, key=lambda x:x[1])
    for check in check_mineral_dic:
        pick_num=0
        for k in range(len(picks)):
            if picks[k]>0:
                pick_num =k
                picks[k]-=1
                break
        for i in range(check[0]*5,check[0]*5+5):
            if i >= check_mineral_cnt:
                break
            
            if minerals[i]=='diamond':
                answer+=arr[pick_num][0]
            elif minerals[i]=='iron':
                answer+=arr[pick_num][1]
            elif minerals[i]=='stone':
                answer+=arr[pick_num][2]

    return answer