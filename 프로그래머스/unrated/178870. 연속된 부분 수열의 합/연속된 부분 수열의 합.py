def solution(sequence, k):
    answer = []
    part_sequence_sum = sequence[0]
    start = 0
    end = 0
    while True:
        if end == len(sequence)-1:
            break
        if part_sequence_sum < k:
            end+=1
            part_sequence_sum += sequence[end]
        elif part_sequence_sum > k:
            part_sequence_sum -= sequence[start]
            start+=1
        else:
            answer.append([start, end, end-start])
            part_sequence_sum -= sequence[start]
            start+=1
    if part_sequence_sum == k:
        answer.append([start, end, end-start])

    elif part_sequence_sum > k:
        while True:
            if part_sequence_sum < k:
                break
            elif part_sequence_sum ==k:
                answer.append([start,end, end-start])
                break
            part_sequence_sum-=sequence[start]
            start+=1
    answer.sort(key = lambda x:(x[2],x[0]))
    return [answer[0][0],answer[0][1]]