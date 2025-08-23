def solution(sequence, k):
    l = r = 0
    answer = [0, len(sequence)]
    ssum = sequence[0]

    while True:
        if ssum < k:
            r += 1
            if r == len(sequence): break
            ssum += sequence[r]
        else:
            if ssum == k:
                if r-l < answer[1]-answer[0]:
                    answer = [l, r]
            ssum -= sequence[l]
            l += 1
    return answer