function solution(priorities, location) {
    let q = priorities.map((priority, idx) => ({idx, priority}));
    let answer = 0;
    
    while (q.length > 0) {
        const current = q.shift();
        if (q.some(item => item.priority > current.priority)) {
            q.push(current)
        } else {
            answer++;
            if (current.idx === location) {
                return answer
            }
            
        }
    }
}