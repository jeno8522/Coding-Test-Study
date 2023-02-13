function solution(queue1, queue2) {
  var answer = -1;
  const sum = (arr) => arr.reduce((a, b) => a + b);
  let sum1 = sum(queue1);
  let sum2 = sum(queue2);
  // let target = parseInt((sum1 + sum2) / 2);

  let i = 0;
  let j = 0;
  let n = queue1.length;
  let m = queue2.length;

  while (i < 2 * n && j < 2 * m && sum1 != sum2) {
    if (sum1 < sum2) {
      sum1 += queue2[j];
      sum2 -= queue2[j];
      queue1.push(queue2[j]);
      j += 1;
    } else {
      sum1 -= queue1[i];
      sum2 += queue1[i];
      queue2.push(queue1[i]);
      i += 1;
    }
  }
  if (sum1 === sum2) {
    answer = i + j;
  }
  return answer;
}

let queue1 = [3, 2, 7, 2];
let queue2 = [4, 6, 5, 1];

console.log(solution(queue1, queue2));
