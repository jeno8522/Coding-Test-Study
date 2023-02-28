package pcsPractice.real;

import java.util.Arrays;

public class NextPermutation {
	static int[]numbers = {1,2,3,4};
	
//	public static boolean np(int[] input) {
//		int n = input.length;
//		
//		// step1. 뒤쪽부터 꼭대기를 찾는다.  (꼭대기 바로 앞이 교환할 자리)
//		int i = n - 1;
//		while(i > 0 && input[i-1] >= input[i]) --i;
//		if(i==0) {	//다음 원소가 없음, 탐색이 끝남, 지금 수가 가장 큰 수
//			return false;
//		}
//		
//		// step2. 꼭대기 바로 앞 (i-1)자리와 교환할 값(더 큰 수)을 뒤쪽부터 찾는다.
//		// 뒤는 오름차순 되어있어서 꼭대기 바로 앞 (i-1)자리보다 큰 값일때의 조건으로 while 돌리면 됨
//		// 꼭대기 바로 앞자리 이므로 뒤쪽에 무조건 더 큰 값이 존재한다.
//		int j = n - 1;
//		while(input[i-1] >= input[j]) --j;
//
//		
//		//step3. 꼭대기 바로 앞 (i-1)자리와 그 자리값보다 한 단계 큰 자리(j) 수와 교환
//		swap(input, i-1, j);
//		
//		//step4. 꼭대기부터 맨 뒤까지 오름차순 정렬
//		int k = n-1;
//		while(i<k) {
//			swap(input, i++, k--);
//		}
//		return true;
//			
//	}
	
	public static boolean np(int[]input) {
		int n = input.length;
		
		int i = n-1;
		while(i > 0 && input[i-1] >= input[i]) --i;
		if(i == 0) return false;
		
		int j = n-1;
		while(input[i-1] >= input[j]) j--;
		
		swap(input, i-1, j);
		
		int k = n-1;
		while(i < k) {
			swap(input,i++,k--);
		}
		return true;
	}
	
	private static void swap(int[] input, int i, int j) {
		int tmp = input[i];
		input[i] = input[j];
		input[j] = tmp;
	}
	public static void main(String[] args) {
		do {
			System.out.println(Arrays.toString(numbers));
		}while(np(numbers));
	}
}
