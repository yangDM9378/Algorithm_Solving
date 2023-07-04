def stage_clear(k, dungeons):
    global used, cnt, answer
    print(k)
    if k<0:
        if cnt > answer:
            answer=cnt
        return
    
    for i in range(len(dungeons)):
        if used[i]==1:continue
        if dungeons[i][0] <= k:
            used[i]=1
            cnt+=1
            stage_clear(k-dungeons[i][1], dungeons)
            cnt-=1
            used[i]=0
    if cnt > answer:
        answer=cnt

def solution(k, dungeons):
    global used, cnt, answer
    answer = -1
    used=[0]*len(dungeons)
    cnt = 0
    stage_clear(k,dungeons)
    return answer