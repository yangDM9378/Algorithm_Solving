function solution(triangle) {
  for (let y = triangle.length - 2; y >= 0; y--) {
    const row = triangle[y];
    const next = triangle[y + 1];
    for (let x = 0, len = row.length; x < len; x++) {
      const a = next[x];
      const b = next[x + 1];
      row[x] += (a > b ? a : b);
    }
  }
  return triangle[0][0];
}