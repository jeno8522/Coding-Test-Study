package s0404;

public class MaxSumArraySlidingWindow {
	/**
	 * 정수로 이루어진 배열에서 길이가 4인 sub 배열의 합계가 가장 큰 서브 배열 구하기 ex ) {2,4,7,10,8,4,5,6,7,1}
	 * 
	 * Sliding Window - 배열이나 리스트 요소의 일정 범위(k개) 값을 비교할 때 사용하면 유용한 알고리즘 - 서브 배열의 요소를
	 * 순회하다 보면 중복되는 요소들이 존재하고 이 중복된 요소를 재사용하는 방법이 슬라이딩 윈도우 알고리즘 - 방법 1. k개의 서브 요소를
	 * 원하는 방법으로 처리한다. 2. 윈도우의 시작부분을 빼고, 윈도우 맨 끝에 새 요소를 추가한다.
	 * 
	 * 시간복잡도 : (k + n - k) = (n)
	 */
	public static void main(String[] args) {
		int[] nums = { 2, 4, 7, 10, 8, 4, 5, 6, 7, 1 };
		int max = 0, sum = 0;
		int k = 4;
		int n = nums.length;

		// 1. k개의 서브 요소를 원하는 방법으로 처리한다.
		for (int i = 0; i < k; i++) {
			sum += nums[i];
		}

		// 2. n-k만큼 반복 돌면서 윈도우의 시작부분을 빼고, 윈도우 맨 끝에 새 요소를 추가한다.
		for (int i = 0, size = n - k; i < size; i++) {
			sum -= nums[i]; // sum에서 window 시작 부분 빼기
			sum += nums[i + k]; // sum에서 window의 끝에 새 요소를 추가하기.
			max = Math.max(max, sum);
		}

		System.out.println(max);
	}

}
