function moveDir(y, x, [dy, dx]) {
    const ny = y + dy;
    const nx = x + dx;
    if (ny < -5 || ny > 5 || nx < -5 || nx > 5) {
        return [y, x];
    }
    return [ny, nx];
}

function solution(dirs) {
    const directDict = {"U":[1, 0], "D":[-1,0], "R":[0,1], "L":[0,-1]}
    let y = 0;
    let x = 0;
    let checked = new Set()
    for (let dir of dirs) {
        const [ny,nx] = moveDir(y, x, directDict[dir])
        if (ny === y && nx ===x) continue;
        const edge = [[y, x], [ny, nx]].sort().map(p => p.join(',')).join("|")
        checked.add(edge)
        y=ny
        x=nx
    }
    return checked.size;
}