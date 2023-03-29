package com.ssafy.dp;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_1149_S1_RGB거리_주창훈 {
	static int n;
	static int[][] dp;
	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		dp = new int[n][3];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 3; j++) {
				dp[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for (int i = 1; i < n; i++) {
			dp[i][0] = Math.min(dp[i-1][1], dp[i-1][2]) + dp[i][0];
			dp[i][1] = Math.min(dp[i-1][0], dp[i-1][2]) + dp[i][1];
			dp[i][2] = Math.min(dp[i-1][0], dp[i-1][1]) + dp[i][2];
		}
		int minCost = Integer.MAX_VALUE;
		for (int i = 0; i < 3; i++) {
			minCost = Math.min(minCost, dp[n-1][i]);
		}
		System.out.println(minCost);
	}

}
