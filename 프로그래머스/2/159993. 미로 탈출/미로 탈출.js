function bfs(maps, start, target) {
  const n = maps.length;
  const m = maps[0].length;
  const visited = Array.from({ length: n }, () => Array(m).fill(false));
  const q = [[start[0], start[1], 0]];
  visited[start[0]][start[1]] = true;

  const directions = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];

  while (q.length > 0) {
    const [x, y, dist] = q.shift();
    if (maps[x][y] === target) return dist;

    for (const [dx, dy] of directions) {
      const nx = x + dx;
      const ny = y + dy;

      if (
        nx >= 0 &&
        nx < n &&
        ny >= 0 &&
        ny < m &&
        !visited[nx][ny] &&
        maps[nx][ny] !== "X"
      ) {
        visited[nx][ny] = true;
        q.push([nx, ny, dist + 1]);
      }
    }
  }
  return -1;
}

function solution(maps) {
  let start, lever, end;
  for (let i = 0; i < maps.length; i++) {
    for (let j = 0; j < maps[0].length; j++) {
      if (maps[i][j] === "S") start = [i, j];
      if (maps[i][j] === "L") lever = [i, j];
      if (maps[i][j] === "E") end = [i, j];
    }
  }

  const s_to_l = bfs(maps, start, "L");
  if (s_to_l === -1) return -1;

  const l_to_e = bfs(maps, lever, "E");
  if (l_to_e === -1) return -1;

  return s_to_l + l_to_e;
}
