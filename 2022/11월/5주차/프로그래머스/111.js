/*
 * str 인자 타입: string | undefined
 */
function solution(...str) {
  let answer = "";
  if (str.length > 0) {
    answer += str;
  } else {
    return answer;
  }
}

console.log(solution("hello")("world")());
