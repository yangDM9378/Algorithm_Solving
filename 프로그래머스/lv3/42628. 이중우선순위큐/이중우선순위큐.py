import heapq

def solution(operations):
    answer = []
    for operation in operations:
        if operation[0] == 'I':
            heapq.heappush(answer, int(operation[2:]))
        elif operation[0] == 'D' and len(answer) >= 1:
            if operation == 'D -1':
                heapq.heappop(answer)
            elif operation == 'D 1':
                answer.pop(answer.index(max(answer)))
    if len(answer) != 0:
        result = [max(answer), answer[0]]
    else:
        result = [0, 0]
    return result