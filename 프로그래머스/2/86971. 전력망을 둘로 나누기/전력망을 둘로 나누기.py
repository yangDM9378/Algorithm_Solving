def solution(n, wires):
    answer = n+1
    for i in range(len(wires)):
        cnt = 0
        used = [0] * len(wires)
        used[i] = 1
        conn = []
        conn.append(wires[i][0])
        while conn:
            st = conn.pop()
            for j in range(len(wires)):
                if used[j] == 1: continue
                if wires[j][0] == st:
                    conn.append(wires[j][1])
                    used[j] = 1
                    cnt += 1
                elif wires[j][1] == st:
                    conn.append(wires[j][0])
                    used[j] = 1
                    cnt += 1
        answer = min(answer, abs(n - 2 - cnt - cnt))
    return answer