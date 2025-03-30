function dfs(dungeons, k, cnt) {
    if (k < 0) {
        li.push(cnt - 1)
        console.log(li)
        return 
    }
    for (let i = 0; i < dungeons.length; i ++) {
        if (used[i] === 0 && k >= dungeons[i][0]) {
            used[i] = 1
            dfs(dungeons, k-dungeons[i][1], cnt+1)
            used[i] = 0
        }
    }
    li.push(cnt)
    return li
}

function solution(k, dungeons) {
    let cnt = 0
    li = Array()
    used = Array.from({length: dungeons.length}, () => 0)
    return Math.max(dfs(dungeons, k, cnt))
}