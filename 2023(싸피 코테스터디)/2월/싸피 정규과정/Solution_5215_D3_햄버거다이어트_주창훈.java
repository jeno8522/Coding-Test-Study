package com.ssafy.combination;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_5215_D3_햄버거다이어트_주창훈 {
	static int max_score;
	static boolean[] isSelected;
	static int[][] info;
	static int limit;
	static int N;
	static int L;

	static void subSet(int cnt, int taste, int calories) {
		if (calories > L) {
			return;
		}
		if (cnt == limit && calories <= L) {
			max_score = Math.max(max_score, taste);
			return;
		} else {
			isSelected[cnt] = true;
			subSet(cnt + 1, taste + info[cnt][0], calories + info[cnt][1]);
			isSelected[cnt] = false;
			subSet(cnt + 1, taste, calories);
		}
	}

	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		for (int test_case = 1; test_case <= T; test_case++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			L = Integer.parseInt(st.nextToken());
			info = new int[N][2];
			max_score = -1;
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				info[i][0] = Integer.parseInt(st.nextToken());
				info[i][1] = Integer.parseInt(st.nextToken());
				for (int j = 1; j <= N; j++) {
					limit = j;
					isSelected = new boolean[N];
					subSet(0, 0, 0);
				}
			}
			System.out.println("#" + test_case + " " + max_score);
		}
	}
}
