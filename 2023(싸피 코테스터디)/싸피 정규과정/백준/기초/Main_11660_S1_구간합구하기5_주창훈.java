package com.ssafy.live03;

import java.util.Scanner;

public class Main_11660_S1_구간합구하기5_주창훈 {
	static int[][] sum;
	static int n;
	static int m;
	static int temp;
	static int start;
	static int end;
	static StringBuilder sb = new StringBuilder();

	static void subTotal(int x1, int y1, int x2, int y2) {

		int result = 0;

		for (int i = x1; i <= x2; i++) {
			result += sum[i - 1][y2] - sum[i - 1][y1 - 1];
		}
		sb.append(result).append("\n");
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int tmp = 0;
		n = sc.nextInt();
		m = sc.nextInt();
		sum = new int[n + 1][n + 1];

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				tmp += sc.nextInt();
				sum[i][j + 1] = tmp;
				if (j == n - 1)
					sum[i + 1][0] = tmp;
			}
		}

		for (int i = 0; i < m; i++) {
			int x1 = sc.nextInt();
			int y1 = sc.nextInt();
			int x2 = sc.nextInt();
			int y2 = sc.nextInt();
			subTotal(x1, y1, x2, y2);

		}
		System.out.print(sb.toString());
	}

}
