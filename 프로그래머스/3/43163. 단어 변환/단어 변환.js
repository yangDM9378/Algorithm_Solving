function chkRule(a, b) {
  let diff = 0;
  for (let i = 0; i < a.length; i++) {
    if (a[i] !== b[i]) {
      diff++;
      if (diff > 1) return false;
    }
  }
  return diff === 1;
}

function solution(begin, target, words) {
  const visited = new Array(words.length).fill(false);
  const queue = [[begin, 0]];
  
  while (queue.length > 0) {
    const [word, cnt] = queue.shift();
    if (word === target) return cnt;
    
    for (let i = 0; i < words.length; i++) {
      if (!visited[i] && chkRule(word, words[i])) {
        visited[i] = true;
        queue.push([words[i], cnt + 1]);
      }
    }
  }
  return 0;
}
