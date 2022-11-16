let fs = require("fs");
// const input = require("fs").readFileSync("예제.txt").toString().split("\n");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let [n, h] = input.shift().split(" ").map(Number);
let arr = [];
let cave = Array(h).fill(0);

for (let e of input) {
  arr.push(parseInt(e));
}
// console.log(arr);
for (let i = 0; i < arr.length; i++) {
  if (i % 2 === 0) {
    cave[h - arr[i]] += 1;
  } else {
    cave[0] += 1;
    cave[arr[i]] -= 1;
    // cave[h] -= 1;
  }
}
let min = cave[0];
let cnt = 1;
for (let i = 1; i < h; i++) {
  cave[i] += cave[i - 1];
  if (cave[i] < min) {
    min = cave[i];
    cnt = 0;
  }
  if (cave[i] === min) {
    cnt += 1;
  }
}

// console.log(...cave);
console.log(min, cnt);
