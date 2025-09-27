function solution(n) {
    let x = 0
    while (true) {
        x = x+1
        if (n % x === 1) {
            return x
        }
    }
}