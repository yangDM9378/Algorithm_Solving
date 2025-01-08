function bfs(y,x,land,used, check_oil) {
    const directs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    const q = [];
    q.push([y, x])
    used[y][x]=1
    let oil = 1
    let min_x = x, max_x = x
    while (q.length > 0) {
        const [y,x] = q.shift()
        for (const [direct_y,direct_x] of directs) {
            const dy = y + direct_y
            const dx = x + direct_x
            if (dy < 0 || dx < 0 || dy >= land.length || dx >=land[0].length) {continue;}
            if (used[dy][dx] === 0 && land[dy][dx]===1) {
                min_x = Math.min(min_x,dx);
                max_x = Math.max(max_x,dx);
                used[dy][dx] = 1;
                oil += 1;
                q.push([dy,dx])
            }
        }   
    }
    for (let idx = min_x; idx <= max_x; idx++) {
        check_oil[idx] += oil
    }
}

function solution(land) {
    const used = Array.from({ length: land.length }, () =>
        Array(land[0].length).fill(0)
    );

    const check_oil = Array(land[0].length).fill(0)
    for (y = 0 ; y < land.length; y++) {
        for (x=0; x < land[0].length; x++) {
            if (land[y][x] === 1 && used[y][x] === 0) {
                bfs(y,x,land,used, check_oil)
            }
        }
    }
    return Math.max(...check_oil)
}