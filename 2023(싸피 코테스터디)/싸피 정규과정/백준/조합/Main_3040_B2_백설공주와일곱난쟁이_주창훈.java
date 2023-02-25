package com.ssafy.hw.step2;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main_3040_B2_백설공주와일곱난쟁이_주창훈 {
	static ArrayList<Integer> arr = new ArrayList<Integer>(9);
	static int sum = 0;

	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < 9; i++) {
			st = new StringTokenizer(br.readLine());
			arr.add(Integer.parseInt(st.nextToken()));
		}
		for (int num : arr) {
			sum += num;
		}
		for (int i = 0; i < 8; i++) {
			for (int j = i + 1; j < 9; j++) {
				if (sum - arr.get(i) - arr.get(j) == 100) {
					for (int k = 0; k < 9; k++) {
						if (k == i || k == j)
							continue;
						sb.append(arr.get(k)).append("\n");
					}
					break;
				}
			}
			if (sb.length() != 0)
				break;
		}
		System.out.print(sb);
	}

}
