package com.ssafy.tree;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution_9229_D3_한빈이와SpotMart_주창훈 {
	static int maxValue;
	static int N;
	static int M;
	static boolean isValid;

	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());

		for (int test_case = 1; test_case <= T; test_case++) {
			isValid = false;
			maxValue = -1;
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());

			st = new StringTokenizer(br.readLine());
			int[] snack = new int[N];
			for (int i = 0; i < N; i++) {
				snack[i] = Integer.parseInt(st.nextToken());
			}
			Arrays.sort(snack);
			int left, right;
			for (int i = 0; i < N - 1; i++) {

				for (int j = 0; j < N - i - 1; j++) {
					left = snack[j];
					right = snack[N - i - 1];
					if (left + right > M)
						break;
					if (maxValue < left + right) {
						maxValue = left + right;
					}

				}
			}
			System.out.printf("#%d %d",test_case,maxValue);
			System.out.println();
		}
	}

}
