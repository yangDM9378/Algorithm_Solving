function solution(storey) {
    let answer = 0;
    
    while (storey) {
        let stor = storey % 10
        if (stor > 5) {
            storey += 10
            answer += (10-stor)
        } else if (stor < 5) {
            answer += stor
        } else {
            if (Math.floor(storey / 10) % 10 > 4) {
                storey += 10
            }
            answer += stor
        }
        storey = Math.floor(storey / 10)
    }
    return answer;
}