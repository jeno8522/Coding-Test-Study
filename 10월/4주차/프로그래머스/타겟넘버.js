function solution(numbers, target) {
  var answer = 0;
  const n = numbers.length;
  function dfs(i, sum, target) {
    if (i == n) {
      if (sum == target) {
        answer += 1;
      }
      return;
    }
    dfs(i + 1, sum + numbers[i], target);
    dfs(i + 1, sum - numbers[i], target);
  }
  dfs(0, 0, target);
  return answer;
}
