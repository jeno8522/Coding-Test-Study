function solution(begin, target, words) {
  let queue = []; //index queue
  let visited = Array(words.length).fill(0);
  const compare = (str1, str2) => {
    let cnt = 0;
    for (let i = 0; i < str1.length; i++) {
      if (str1[i] !== str2[i]) cnt += 1;
      if (cnt > 1) return false;
    }
    return true;
  };
  let cnt = 1;
  for (let i = 0; i < words.length; i++) {
    if (compare(begin, words[i])) {
      queue.push([i, cnt]);
      visited[i] = 1;
    }
  }
  while (queue.length) {
    let [idx, cnt] = queue.shift();
    let origin = words[idx];
    if (words[idx] === target) return cnt;
    for (let i = 0; i < words.length; i++) {
      if (!visited[i]) {
        if (compare(origin, words[i])) {
          queue.push([i, cnt + 1]);
          visited[i] = 1;
        }
      }
    }
  }
  return 0;
}

let words = ["hot", "dot", "dog", "lot", "log", "cog"];
let begin = "hit";
let target = "cog";
console.log(solution(begin, target, words));
