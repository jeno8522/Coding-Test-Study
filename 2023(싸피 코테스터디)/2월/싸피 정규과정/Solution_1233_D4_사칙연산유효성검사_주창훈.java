package com.ssafy.tree;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class SWEA_1233_d4_사칙연산유효성_주창훈 {
	static int N;

	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for (int test_case = 1; test_case <= 10; test_case++) {
			N = Integer.parseInt(br.readLine());
			boolean ans = true;
			if (N % 2 == 0)
				ans = false;
			for (int i = 0; i < N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				int node = Integer.parseInt(st.nextToken());
				for (int j = 0; j < st.countTokens() - 1; j++) {
					System.out.println(j);
					String now = st.nextToken();
					if (!charcheck(now.charAt(0))) {
						ans = false;
					}
				}
			}
			System.out.print("#" + test_case + " ");
			if (ans == false) {
				System.out.println(0);
			} else {
				System.out.println(1);
			}
		}

	}

	public static boolean charcheck(char c) {
		if (c == '*' || c == '+' || c == '-' || c == '/') {
			return true;
		}
		return false;
	}
}