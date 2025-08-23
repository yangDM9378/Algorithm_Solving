def solution(sequence, k):
    n = len(sequence)
    s = e = 0
    ssum = sequence[0]
    # best: (start, end) inclusive. 초기값은 불가능한 최장 길이로 설정
    best = (0, n)  

    while True:
        # 합이 정확히 k이면 후보 갱신
        if ssum == k:
            # 더 짧거나, 길이가 같으면 시작 인덱스가 작은 쪽 선택
            if (best[1] - best[0]) > (e - s) or (
                (best[1] - best[0]) == (e - s) and s < best[0]
            ):
                best = (s, e)

        # 윈도우 조정
        if ssum >= k:
            ssum -= sequence[s]
            s += 1
            # s가 e를 넘어가면 윈도우를 다시 1칸짜리로 정렬
            if s > e and s < n:
                e = s
                ssum = sequence[s]
        else:  # ssum < k
            e += 1
            if e == n:
                break
            ssum += sequence[e]

    return [best[0], best[1]]
