function GCD(a,b) {
    while (true) {
        if (a % b === 0) {
            return b
        }
        let tmp = a % b
        a = b
        b = tmp
    }
}

function solution(arr) {
    let a,b
    let arr_sort = arr.sort((a,b) => a-b)
    a = arr_sort.pop()
    while (arr_sort.length !== 0) {
        b = arr_sort.pop()
        let tmp = GCD(a,b)
        a = a * b / GCD(a,b)
        }
    return a;
}