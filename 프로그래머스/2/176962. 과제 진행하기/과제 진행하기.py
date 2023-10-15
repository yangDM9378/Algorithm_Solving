from collections import deque
def solution(plans):
    answer = []
    task = []
    rest = []
    for plan in plans:
        new_plan=[]
        new_plan.append(int(plan[1][:2])*60+int(plan[1][3:]))
        new_plan.append(int(plan[2]))
        new_plan.append(plan[0])
        task.append(new_plan)
    task.append([1440,2448,'end'])
    task.sort(key=lambda x:x[0])
    q=deque(task)
    current_time, time, work = q.popleft()
    while q:
        next_start, next_time, next_work = q.popleft()
        end_time = current_time+time
        if next_start == end_time:
            answer.append(work)
        elif next_start < end_time:
            rest.append([time-(next_start-current_time),work])
        else:
            answer.append(work)
            current_rest_time = next_start-(end_time)
            while rest:
                rest_time, rest_work = rest.pop()
                if current_rest_time >= rest_time:
                    answer.append(rest_work)
                    current_rest_time = current_rest_time - rest_time 
                elif current_rest_time < rest_time:
                    rest.append([rest_time-current_rest_time, rest_work])
                    break
        current_time, time, work = next_start, next_time, next_work
    while rest:
        rest_time,rest_work = rest.pop()
        answer.append(rest_work)
    return answer