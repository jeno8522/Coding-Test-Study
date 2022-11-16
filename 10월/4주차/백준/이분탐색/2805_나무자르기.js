let fs = require("fs");
// const input = require("fs").readFileSync("예제.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");
const [N, M] = input.shift().split(" ");
const trees = input[0]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);

function solution(arr, target) {
  let start = 0;
  let end = arr[arr.length - 1];
  let answer = Number.MIN_SAFE_INTEGER;
  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    let sum = 0;
    for (let x of arr) {
      if (x > mid) sum += x - mid;
    }

    if (sum >= target) {
      if (mid > answer) answer = mid;
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }

  return answer;
}

console.log(solution(trees, M));
// console.log(input);
// console.log(N, M);
