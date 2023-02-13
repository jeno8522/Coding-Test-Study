let fs = require("fs");
const input = require("fs").readFileSync("예제.txt").toString().split("\n");
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [N, M] = input.shift().split(" ");
const arr = input[0].split(" ").map(Number);
let vm = Math.max(...arr);
let start = vm;
let end = arr.reduce((sum, cur) => sum + cur, 0);
let res = 1000000000;

while (start <= end) {
  let mid = Math.floor((start + end) / 2);
  let cnt = 1;
  let tmp = 0;
  for (let num of arr) {
    if (tmp + num <= mid) tmp += num;
    else {
      cnt += 1;
      tmp = num;
    }
    if (cnt > M) break;
  }
  if (cnt > M) {
    start = mid + 1;
  } else if (cnt <= M) {
    end = mid - 1;
    if (mid >= vm) {
      res = Math.min(mid, res);
    }
  }
}
console.log(res);
// console.log(N, M);
// console.log(arr);
