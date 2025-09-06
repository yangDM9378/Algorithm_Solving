function solution(n, computers) {
    const used = Array(n).fill(false);
    const dfs = (start) => {
        const stack = [start];
        used[start] = true;
        while (stack.length) {
            const cur = stack.pop()
            for (let nxt = 0; nxt < n; nxt++) {
                if (cur === nxt) continue;
                if (computers[cur][nxt] === 1 && !used[nxt]) {
                    used[nxt] = true;
                    stack.push(nxt)
                }
            }
        }
    };
    
    let cnt = 0;
    for (let i = 0; i < n; i++) {
        if (!used[i]) {
            dfs(i);
            cnt++;
        }
    }
    return cnt;
}