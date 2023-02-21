package com.ssafy.temporary;

import java.util.Arrays;

public class SubsetTest {
	static int N = 7;
	static int M = 3;
	static int[] numbers = { 1, 2, 3, 4, 5, 6, 7 };
	static boolean[] isSelected = new boolean[7];
	static int[] res = new int[3];

	public static void permutation(int cnt) {
		if (cnt == N) {
			System.out.println(Arrays.toString(res));
			return;
		}
		for (int i = 0; i < N; i++) {
			if (isSelected[i])
				continue;
			isSelected[i] = true;
			res[cnt] = i;
			permutation(cnt + 1);
			isSelected[i] = false;

		}
	}

	public static void subset(int cnt) {
		if (cnt == N) {
			for (int i = 0; i < N; i++) {
				System.out.print(isSelected[i] ? numbers[i] : "X");
				System.out.print(" ");
			}
			System.out.println();
			return;
		} else {
			isSelected[cnt] = true;
			subset(cnt + 1);
			isSelected[cnt] = false;
			subset(cnt + 1);
		}
	}

	public static void combination(int cnt, int start) {
		if (cnt == M) {
			System.out.println(Arrays.toString(res));
			return;
		}
		for (int i = start; i < N; i++) {
			res[cnt] = numbers[i];
			combination(cnt + 1, i + 1);
		}
	}
//	static void combination1(int cnt, int start) {
//		if (cnt == M) {
//			for (int num : numbers) {
//				sb.append(num).append(" ");
//			}
//			sb.append("\n");
//			return;
//		}
//		for (int i = start; i <= N; i++) {
//			numbers[cnt] = i;
//			combination1(cnt + 1, i + 1);
//		}
//	}

	public static void main(String[] args) {
//		subset(0);
//		permutation(0);
		combination(0, 0);
	}

}
