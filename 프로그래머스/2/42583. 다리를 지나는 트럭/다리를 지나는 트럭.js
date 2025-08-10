function solution(bridge_length, weight, truck_weights) {
  const waiting = [...truck_weights];
  const bridgeQueue = [];
  let time = 0;
  let onBridge = 0;

  while (waiting.length > 0 || onBridge > 0) {
    time += 1;
    if (bridgeQueue.length && bridgeQueue[0].exit === time) {
      onBridge -= bridgeQueue[0].w;
      bridgeQueue.shift();
    }
    if (waiting.length && onBridge + waiting[0] <= weight && bridgeQueue.length < bridge_length) {
      const w = waiting.shift();
      onBridge += w;
      bridgeQueue.push({ w, exit: time + bridge_length });
    }
  }

  return time;
}