def solution(n, t, m, timetable):
    answer = ''
    bus_dic = {}
    arr=[]
    for i in range(n):
        bus_dic[540+t*i] = []
    for time in timetable:
        sec_time = int(time[:2])*60+int(time[3:])
        arr.append(sec_time)
    arr.sort()
    for time in arr:
        for bus_time in bus_dic:
            if time <= bus_time and len(bus_dic[bus_time])<m:
                bus_dic[bus_time].append(time)
                break
    for k,v in bus_dic.items():
        if len(v)<m:
            answer = k
        else:
            answer = max(v)-1
            
    h=str(answer//60)
    s=str(answer%60)
    if len(h)==1:
        h='0'+h
    if len(s)==1:
        s='0'+s
    result = h+':'+s
    return result