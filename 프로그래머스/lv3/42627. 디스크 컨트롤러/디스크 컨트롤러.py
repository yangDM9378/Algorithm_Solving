import heapq
def solution(jobs):
    job_n = len(jobs)
    heapq.heapify(jobs)
    start,time = heapq.heappop(jobs)
    hq = []
    heapq.heappush(hq,[time,start])
    current_time = start
    answer = 0
    while hq:
        time, start = heapq.heappop(hq)
        answer += (current_time-start)+time
        current_time+=time
        print(current_time)
        while jobs:
            start, time = heapq.heappop(jobs)
            if len(hq)==0:
                heapq.heappush(hq,[time,start])
            elif start<current_time:
                heapq.heappush(hq,[time,start])
            else:
                heapq.heappush(jobs, [start,time])
                break
    return answer//job_n