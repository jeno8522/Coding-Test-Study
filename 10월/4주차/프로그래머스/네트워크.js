function solution(n, computers) {
  var answer = 0;
  let visited = Array.from({ length: n }, () => 0);
  function dfs(num) {
    visited[num] = 1;
    for (let i = 0; i < n; i++) {
      if (i === num) continue;
      if (visited[i] === 0 && computers[num][i] == 1) {
        // console.log(visited);
        dfs(i);
      }
    }
  }
  for (let i = 0; i < n; i++) {
    if (visited[i] === 0) {
      dfs(i);
      // console.log(visited);
      answer += 1;
    }
  }
  return answer;
}

let n = 3;
let arr = [
  [1, 1, 0],
  [1, 1, 0],
  [0, 0, 1],
];
console.log(solution(n, arr));
// console.log(solution(n, arr));
