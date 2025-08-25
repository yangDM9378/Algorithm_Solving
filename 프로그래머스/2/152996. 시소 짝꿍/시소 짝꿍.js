function solution(weights) {
    let answer = 0;
    const weightCount = new Map()
    for (const w of weights) {
        weightCount.set(w, (weightCount.get(w) || 0) + 1);
    }
    
    for (const [w, count] of weightCount.entries()) {
        answer += (count * (count-1)) / 2;
        const ratios = [4/3,2/3,2];
        for (const r of ratios) {
            const target = w * r;
            if (weightCount.has(target)) {
                answer += count * weightCount.get(target)
            }
        }
    }
    
    return answer;
}