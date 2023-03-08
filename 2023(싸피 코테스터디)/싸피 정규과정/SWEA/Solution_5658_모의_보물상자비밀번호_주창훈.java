package com.ssafy.hw.step2;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Solution_5658_모의_보물상자비밀번호_주창훈 {
	static int N, K;
	static ArrayDeque<Integer> queue;
	static HashSet<Integer> set;

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		for (int test_case = 1; test_case <= T; test_case++) {

			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());

			String str = br.readLine();
			queue = new ArrayDeque<>();
			set = new HashSet<>();

			for (int i = 0; i < N / 4; i++) {
				for (int j = i; j < i + N; j += N / 4) {
					StringBuilder sb = new StringBuilder();
					for (int k = j; k < j + N / 4; k++) {
						int idx = k % N;
						sb.append(str.charAt(idx));
					}
					int num = Integer.parseInt(sb.toString(), 16);
					set.add(num);
				}
			}
			ArrayList<Integer> tmp = new ArrayList<>(set);
			Collections.sort(tmp, Collections.reverseOrder());
			System.out.println("#" + test_case + " " + tmp.get(K - 1));
		}
	}

}
