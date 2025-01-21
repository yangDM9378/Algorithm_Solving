function solution(scores) {
    let answer = 1;
    let [wanhoAt, wanhoEx] = scores[0];
    scores.sort((a, b) => b[0] - a[0] || a[1] - b[1]);

    let passNum = 0;
    
    for (let i = 0; i < scores.length; i++) {
        let [checkAt, checkEx] = scores[i];

        if (wanhoAt < checkAt && wanhoEx < checkEx) {
            return -1;
        }

        if (passNum <= checkEx) {
            if (wanhoAt + wanhoEx < checkAt + checkEx) {
                answer++;
            }
            passNum = checkEx;
        }
    }

    return answer;
}