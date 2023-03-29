package com.ssafy.dp;

import java.util.Scanner;

public class Main_1463_S3_1로만들기_주창훈 {
	static int res = Integer.MAX_VALUE;

	static void findOne(int val, int cnt) {
		if (cnt >= res) return;
		if (val == 1) {
			res = Math.min(res, cnt);
			return;
		}
		if (val % 3 == 0)
			findOne(val / 3, cnt + 1);
		if (val % 2 == 0)
			findOne(val / 2, cnt + 1);
		findOne(val - 1, cnt + 1);
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		findOne(n, 0);
		System.out.println(res);
	}

}
