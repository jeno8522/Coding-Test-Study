package s0404;

public class MaxSumArray1 {
	/**
	 * 정수로 이루어진 배열에서 길이가 4인 sub 배열의 합계가 가장 큰 서브 배열 구하기 ex ) {2,4,7,10,8,4,5,6,7,1}
	 * 
	 * 시간 복잡도 : (n-k+1)*k
	 * 
	 * BOJ 15961 회전초밥 N : 3,000,000 K : 3000 (N - K + 1) * K -> 브루트포스 는 90억이라 터짐
	 * 
	 */
	public static void main(String[] args) {
		int[] nums = { 2, 4, 7, 10, 8, 4, 5, 6, 7, 1 };
		int max = 0, sum = 0;
		int k = 4;
		int n = nums.length;

		for (int i = 0; i < n - k; i++) {
			sum = 0;
			for (int j = i; j < i + k; j++) {
				sum += nums[j];
			}
			max = Math.max(max, sum);
		}
		System.out.println(max);
	}

}
