function solution(n) {
    var answer = 0;
    let bin_n = n.toString(2)
    const bin_num = bin_n.split('').filter(el => el === '1').length;
    while (true) {
        n = n+1
        n.toString(2)
        let bin_n = n.toString(2)
        const new_bin_num = bin_n.split('').filter((el) => (el==='1')).length
        if (bin_num === new_bin_num) {
            return n
        }
    }
}