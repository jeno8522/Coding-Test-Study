function solution(maps) {
  //최단 거리는 bfs
  var answer = 0;
  const dr = [0, 1, 0, -1];
  const dc = [1, 0, -1, 0];
  const n = maps.length;
  const m = maps[0].length;
  let queue = [];
  const isRoad = (nextY, nextX, row, col) =>
    nextY < 0 || nextX < 0 || nextY > row || nextX > col;

  function bfs(r, c, cnt) {
    queue.push([r, c, cnt]);
    while (queue.length) {
      let [r, c, cnt] = queue.shift();
      // maps[r][c] = 0;  시간초과
      if (r === n - 1 && c === m - 1) return cnt;

      for (let i = 0; i < 4; i++) {
        let nr = r + dr[i];
        let nc = c + dc[i];
        if (isRoad(nr, nc, n - 1, m - 1)) {
          continue;
        }
        if (maps[nr][nc] === 0) {
          continue;
        }
        queue.push([nr, nc, cnt + 1]);
        maps[nr][nc] = 0;
      }
    }
  }
  answer = bfs(0, 0, 1);
  if (!answer) answer = -1;
  return answer;
}
