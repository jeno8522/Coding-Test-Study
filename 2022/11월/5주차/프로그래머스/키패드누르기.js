function solution(numbers, hand) {
  var answer = "";
  const mode = hand.slice(0, 1).toUpperCase();
  const rNum = "369";
  const lNum = "147";
  const nNum = "2580";
  let rIdx = -1;
  let lIdx = -1;
  const calDis = (idx, now) => {
    if (idx === -1 && now === 0) return 1;
    if (idx === -1 && now === 8) return Math.ceil(Math.sqrt(2));
    if (idx === -1 && now === 5) return Math.ceil(Math.sqrt(5));
    if (idx === -1 && now === 2) return Math.ceil(Math.sqrt(10));
    if (
      (idx === 1 && now === 2) ||
      (idx === 4 && now === 5) ||
      (idx === 7 && now === 8)
    ) {
      return 1;
    } else if (
      (idx === 3 && now === 2) ||
      (idx === 6 && now === 5) ||
      (idx === 9 && now === 8)
    ) {
      return 1;
    } else {
      let tmp_idx = 0;
      let tmp_now = 0;

      if (idx === 1 || idx === 3 || idx === 2) tmp_idx = 0;
      else if (idx === 4 || idx === 6 || idx === 5) tmp_idx = 1;
      else if (idx === 7 || idx === 9 || idx === 8) tmp_idx = 2;
      else if (idx === 0) tmp_idx = 3;
      if (now === 2) tmp_now = 0;
      else if (now === 5) tmp_now = 1;
      else if (now === 8) tmp_now = 2;
      else if (now === 0) tmp_now = 3;
      if ("2580".indexOf(idx) > -1) {
        return Math.abs(tmp_idx - tmp_now);
      } else {
        return Math.ceil(
          Math.sqrt(
            1 + Math.abs(tmp_idx - tmp_now) * Math.abs(tmp_idx - tmp_now)
          )
        );
      }
    }
  };
  for (let now of numbers) {
    if (rNum.indexOf(String(now)) > -1) {
      answer += "R";
      rIdx = now;
    } else if (lNum.indexOf(String(now)) > -1) {
      answer += "L";
      lIdx = now;
    } else if (nNum.indexOf(String(now)) > -1) {
      let rRes = calDis(rIdx, now);
      let lRes = calDis(lIdx, now);
      // if (lIdx === 4 && rIdx === 2 && now === 5) console.log(rRes, lRes);
      if (rRes === lRes) {
        answer += mode;
        if (mode === "R") rIdx = now;
        else if (mode === "L") lIdx = now;
      } else if (rRes < lRes) {
        answer += "R";
        rIdx = now;
      } else if (rRes > lRes) {
        answer += "L";
        lIdx = now;
      }
    }
  }
  return answer;
}

let numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5];
let hand = "right";

console.log(solution(numbers, hand));
