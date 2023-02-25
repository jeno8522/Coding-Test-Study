package com.ssafy.live03;

import java.util.Scanner;

public class Main_11659_S3_구간합구하기4_주창훈 {
	static int[] numbers;
	static int[] sum;
	static int n;
	static int m;
	static int temp;
	static int start;
	static int end;
	static StringBuilder sb = new StringBuilder();

	static void subTotal(int start, int end) {
		if (start == 1)
			sb.append(sum[end - 1]);
		
		else
			sb.append(sum[end - 1] - sum[start - 2]);
		sb.append("\n");

	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		numbers = new int[n];
		sum = new int[n];
		for (int i = 0; i < n; i++) {
			numbers[i] = sc.nextInt();
		}

		temp = 0;
		for (int i = 0; i < n; i++) {
			temp += numbers[i];
			sum[i] = temp;
		}

		for (int i = 0; i < m; i++) {
			int start = sc.nextInt();
			int end = sc.nextInt();
			subTotal(start, end);
			
		}
		System.out.print(sb.toString());

	}

}
