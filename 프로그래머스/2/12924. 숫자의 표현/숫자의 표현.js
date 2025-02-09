function solution(n) {
    let cnt = 1
    let ssum = 0
    let start = 1
    for (i=1; i < n+1; i++) {
        if (ssum === n) {
            cnt++
        }
        ssum += i
        while (ssum > n) {
            ssum -= start++
        }

    }
    return cnt;
}