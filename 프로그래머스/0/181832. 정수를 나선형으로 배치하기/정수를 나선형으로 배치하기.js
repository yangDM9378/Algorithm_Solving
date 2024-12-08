function solution(n) {
    let answer = Array.from({length: n}, () => Array(n).fill(0));
    const direct = [[0, 1],[1, 0],[0, -1], [-1, 0]]
    let x = 0, y = 0, dir = 0
    
    for (i=1; i<n**2+1; i++) {
        answer[x][y] = i
        const nx = x+direct[dir][0]
        const ny = y+direct[dir][1]
        if (nx < 0 || nx > n - 1 || ny < 0 || ny > n - 1 || answer[nx][ny] != 0) {
            dir = (dir + 1) % 4
    
        }
        x = x + direct[dir][0]
        y = y + direct[dir][1]
    }

    
    return answer;
}