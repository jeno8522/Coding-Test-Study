package com.ssafy.dp;

import java.util.Arrays;
import java.util.Scanner;

public class Main_2839_S4_설탕배달_주창훈 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] dp = new int[5001];
		Arrays.fill(dp, 5000);
		
		if (n == 4) {
			System.out.println(-1);
		} else {
			dp[3] = 1;
			dp[5] = 1;
			if (n >= 6) {
				for (int i = 6; i <= n; i++) {
					dp[i] = Math.min(dp[i - 3] + 1, dp[i - 5] + 1);
				}
			}
			if (dp[n] >= 5000) {
				System.out.println(-1);
			} else {
				System.out.println(dp[n]);
			}
		}
	}

}
