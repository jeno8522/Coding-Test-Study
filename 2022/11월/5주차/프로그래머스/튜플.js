function solution(s) {
  var answer = [];
  let tuples = s.slice(2, -2).split("},{");
  const n = tuples.length;
  let cntD = {};

  for (let e of tuples) {
    let tmp = e.split(",");
    for (let num of tmp) {
      if (cntD[num]) {
        cntD[num] += 1;
      } else {
        cntD[num] = 1;
      }
    }
  }
  answer = [...Object.entries(cntD)];
  // console.log(answer);
  answer.sort((a, b) => b[1] - a[1]);

  answer = answer.map((e) => parseInt(e[0]));
  return answer;
}

let s = "{{2},{2,1},{2,1,3},{2,1,3,4}}";
console.log(solution(s));
