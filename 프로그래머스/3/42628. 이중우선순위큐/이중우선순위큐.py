import heapq

def solution(operations):
    li = []
    revert_li = []
    for operation in operations:
        if operation[0] == 'I':
            heapq.heappush(li, int(operation[2:]))
            heapq.heappush(revert_li, -int(operation[2:]))
        elif len(li) != 0 and operation[0] == 'D':
            if operation[1:] == ' -1':
                chk_num = heapq.heappop(li)
                revert_li.remove(-chk_num)
            elif operation[1:] == ' 1':
                chk_num = heapq.heappop(revert_li)
                li.remove(-chk_num)
    if len(li) == 0:
        answer = [0,0]
    elif len(li) == 1:
        num = heapq.heappop(li)
        answer = [num,num]
    else:
        answer = [-heapq.heappop(revert_li), heapq.heappop(li)]
    return answer