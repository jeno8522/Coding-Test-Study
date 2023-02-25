package com.ssafy.subset;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Solution_1225_D3_암호생성기_주창훈 {
	static Deque<Integer> password;
	static StringBuilder sb;
	static StringTokenizer st;
	static BufferedReader br;
	static int t;

	static boolean cycle(int num) {

		int tmp = password.pollFirst();
		tmp -= num;
		if (tmp <= 0) {
			tmp = 0;
			password.addLast(tmp);
			return false;
		}
		password.addLast(tmp);
		return true;
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		br = new BufferedReader(new InputStreamReader(System.in));

		for (int test_case = 1; test_case <= 10; test_case++) {
			password = new ArrayDeque<>();
			sb = new StringBuilder();
			t = Integer.parseInt(br.readLine());
			String str = br.readLine();
			st = new StringTokenizer(str, " ");

			for (int i = 0; i < 8; i++) {
				int num = Integer.parseInt(st.nextToken());
				password.addLast(num);
			}

			int phase = 1;
			while (true) {

				if (cycle(phase) == false) {
					break;
				}
				phase++;
				if (phase == 6)
					phase = 1;

			}
			System.out.print("#" + test_case + " ");
			for (int i = 0; i < 8; i++) {
				System.out.print(password.pollFirst() + " ");
			}
			System.out.println();

		}

	}

}
