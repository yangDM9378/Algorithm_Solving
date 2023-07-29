import math
def solution(n, stations, w):
    start = 1
    answer =0
    W=2*w+1
    for station in stations:
        answer+=math.ceil((station-w-start)/W)
        start=station+w+1

    if start <= n:
        answer+=math.ceil((n-start+1)/W)
    return answer