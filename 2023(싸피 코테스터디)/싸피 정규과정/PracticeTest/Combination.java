package com.ssafy.temporary;

import java.util.Arrays;

public class Combination {
	static int[] arr = { 1, 2, 3, 4, 5, 6 };
	static int N = 6, R = 3;
	static int[] res = new int[6];
	static boolean[] isSelected;

	public static void combination(int cnt, int start) {
		if (cnt == R) {
			System.out.println(Arrays.toString(res));
			return;
		}
		for (int i = start; i < N; i++) {
			res[cnt] = arr[i];
			combination(cnt + 1, i + 1);
		}
	}

	public static void permutation(int cnt) {
		if (cnt == R) {
			System.out.println(Arrays.toString(res));
			return;
		}
		for (int i = 0; i < N; i++) {
			if (isSelected[i])
				continue;
			res[cnt] = arr[i];
			isSelected[i] = true;
			permutation(cnt + 1);
			isSelected[i] = false;
		}
	}

	public static void subset(int cnt) {
		if (cnt == N) {
			for (int i = 0; i < N; i++) {
				System.out.print(isSelected[i] ? arr[i] : "X");
			}
			System.out.println();
			return;
		}

		isSelected[cnt] = true;
		subset(cnt + 1);
		isSelected[cnt] = false;
		subset(cnt + 1);

	}

	public static void main(String[] args) {
//		combination(0,0);
//		permutation(0);
		isSelected = new boolean[N];
		subset(0);
	}

}
