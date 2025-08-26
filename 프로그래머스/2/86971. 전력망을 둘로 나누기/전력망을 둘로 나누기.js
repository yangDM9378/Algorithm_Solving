function solution(n, wires) {
    let answer = n + 1;
    
    for (let i = 0; i < wires.length; i++) {
        let cnt = 0;
        let used = new Array(wires.length).fill(0);
        used[i] = 1;
        let conn = [wires[i][0]];
        
        while (conn.length > 0) {
            let st = conn.pop();
            for (let j = 0; j < wires.length; j++) {
                if (used[j] === 1) continue;
                if (wires[j][0] === st) {
                    conn.push(wires[j][1]);
                    used[j] = 1;
                    cnt += 1;
                } else if (wires[j][1] === st) {
                    conn.push(wires[j][0]);
                    used[j] = 1;
                    cnt += 1;
                }
            }
        }
        
        answer = Math.min(answer, Math.abs(n - 2 - cnt - cnt));
    }
    
    return answer;
}