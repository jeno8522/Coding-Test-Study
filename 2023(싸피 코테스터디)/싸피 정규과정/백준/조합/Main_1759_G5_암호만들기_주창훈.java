package com.ssafy.hw.step2;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_1759_G5_암호만들기_주창훈 {

	static int L, C;
	static String[] base;
	static ArrayList<String> code = new ArrayList<>();

	static int checkVowel() {
		int vowelCnt = 0;
		for (String s : code) {
			if (s.equals("a") || s.equals("e") || s.equals("i") || s.equals("o") || s.equals("u"))
				vowelCnt++;
		}
		return vowelCnt;
	}

	static void combination(int cnt, int start) {
		if (cnt == L) {
			int v = checkVowel();
//			System.out.println(code.toString());
			if (v >= 1 && v <= L - 2) {
				for (String s : code) {
					System.out.print(s);
				}
				System.out.println();
			}
			return;
		}
		for (int i = start; i < C; i++) {
			code.add(base[i]);
			combination(cnt + 1, i + 1);
			code.remove(code.size() - 1);
		}
	}

	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		L = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		String str = br.readLine();
		base = str.split(" ");
		Arrays.sort(base);

		combination(0, 0);
	}

}