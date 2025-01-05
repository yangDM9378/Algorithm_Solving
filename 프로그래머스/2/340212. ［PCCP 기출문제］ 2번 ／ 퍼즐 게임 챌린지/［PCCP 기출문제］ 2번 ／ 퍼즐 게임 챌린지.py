def solution(diffs, times, limit):
    s,e = 1, max(diffs)+1
    
    while e > s:
        chk_level = (e+s) // 2
        chk_time = 0
        
        for i in range(len(diffs)):
            if i == 0:
                time_cur=times[0]
                time_pre=0
            else:
                time_cur=times[i]
                time_pre=times[i-1]
            used_time = time_cur + max(0,(diffs[i]-chk_level))*(time_cur+time_pre)
            chk_time += used_time
            
        if chk_time <= limit:
            e=chk_level
        else:
            s=chk_level+1
    return s

    