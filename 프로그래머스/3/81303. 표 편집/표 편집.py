def solution(n, k, cmd):
    answer = ['O'] * n
    prev = [i - 1 for i in range(n)]
    next = [i + 1 for i in range(n)]
    next[n - 1] = -1  # 마지막 노드의 next는 없음

    removed = []

    for c in cmd:
        if c[0] == 'U':
            x = int(c[2:])
            for _ in range(x):
                k = prev[k]
        elif c[0] == 'D':
            x = int(c[2:])
            for _ in range(x):
                k = next[k]
        elif c[0] == 'C':
            removed.append((k, prev[k], next[k]))  # 현재 커서 위치와 주변 링크 정보 저장
            answer[k] = 'X'

            # 링크 끊기
            if prev[k] != -1:
                next[prev[k]] = next[k]
            if next[k] != -1:
                prev[next[k]] = prev[k]

            # 커서 이동
            k = next[k] if next[k] != -1 else prev[k]
        elif c[0] == 'Z':
            idx, p, n_ = removed.pop()
            answer[idx] = 'O'

            if p != -1:
                next[p] = idx
            if n_ != -1:
                prev[n_] = idx

    return ''.join(answer)
