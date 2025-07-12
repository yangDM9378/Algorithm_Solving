from collections import deque
import math
def solution(players, m, k):
    answer = 0
    server_num = 1
    server_list = deque()
    for i in range(len(players)):
        if len(server_list) != 0:
            end_time, end_server_num = server_list.popleft()
            if end_time < i:
                server_num -= end_server_num
            else:
                server_list.appendleft([end_time, end_server_num])
        player = players[i]
        if player < (server_num)*m:continue
        need_server_num = math.ceil((player+1)/m)
        add_server_num = need_server_num - server_num
        server_num += add_server_num
        server_end = [i+k-1, add_server_num]
        server_list.append(server_end)
        answer += add_server_num
    return answer