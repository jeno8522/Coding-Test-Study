package com.ssafy.live03;

import java.util.Scanner;

public class Main_15650_S3_N과M2_주창훈 {
	private static int N;
	private static int M;
	static StringBuilder sb = new StringBuilder();

	private static int[] numbers;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		numbers = new int[M];
		comb(0, 1);
		System.out.println(sb.toString());
	}

	private static void comb(int cnt, int start) {
		if (cnt == M) {
			for (int i : numbers) {
				sb.append(i).append(" ");
			}
			sb.append("\n");
			return;
		}
		for (int i = start; i <= N; i++) {
			numbers[cnt] = i;
			comb(cnt + 1, i + 1);

		}
	}
}
