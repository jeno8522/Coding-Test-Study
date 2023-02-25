package com.ssafy.live04;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_2961_S2_도영이가만든맛있는음식_주창훈 {
	static int N;
	static int[][] taste;
	static boolean[] isSelected;
	static int min;

	static void makeSubset(int cnt) {
		if (cnt == N) {
			isBestTaste();
			return;
		}
		isSelected[cnt] = true;
		makeSubset(cnt + 1);
		isSelected[cnt] = false;
		makeSubset(cnt + 1);
	}

	static void isBestTaste() {
		int bitter = 0;
		int sour = 1;
		for (int i = 0; i < N; i++) {
			if (isSelected[i]) {
				sour *= taste[0][i];
				bitter += taste[1][i];
			}
		}
		if (bitter == 0 && sour == 1)
			return;
		int val = Math.abs(sour - bitter);
		if (min > val)
			min = val;
	}

	public static void main(String[] args) throws IOException {
		StringTokenizer st;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		N = Integer.parseInt(br.readLine());
		isSelected = new boolean[N];
		taste = new int[2][N];
		min = Integer.MAX_VALUE;

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			taste[0][i] = Integer.parseInt(st.nextToken());
			taste[1][i] = Integer.parseInt(st.nextToken());
		}
//		System.out.println(N);
//		for (int[] t : taste) {
//			for ( int e : t) {
//				System.out.println(e);
//			}
//		}
		makeSubset(0);

		System.out.println(min);

	}

}
