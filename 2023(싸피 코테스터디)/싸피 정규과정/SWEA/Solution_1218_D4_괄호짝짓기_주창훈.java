package com.ssafy.live04;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Solution_1218_D4_괄호짝짓기_주창훈 {
	static Deque<Character> pare;
	static int N;

	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		for (int test_case = 1; test_case <= 10; test_case++) {
			StringBuilder sb = new StringBuilder();
			StringTokenizer st = new StringTokenizer(br.readLine());
			pare = new ArrayDeque<>();
			int res = 1;

			N = Integer.parseInt(st.nextToken());
			st = new StringTokenizer(br.readLine());
			String str = st.nextToken();

			for (int i = 0; i < N; i++) {
				Character cur = str.charAt(i);
				res = 1;
				
				if (cur == '(' || cur == '{' || cur == '[' || cur == '<') {
					pare.addLast(cur);
				}else {
					if(pare.isEmpty()) {
						res = 0;
					}else {
						if(cur == ')') {
							if(pare.pollLast()=='(') continue;
							else {
								res = 0;
								break;
							}
						} else if(cur == '}') {
							if(pare.pollLast()=='{') continue;
							else {
								res = 0;
								break;
							}
						} else if(cur == ']') {
							if(pare.pollLast()=='[') continue;
							else {
								res = 0;
								break;
							}
						} else if(cur == '>') {
							if(pare.pollLast()=='<') continue;
							else {
								res = 0;
								break;
							}
						}
					}
				}
			}
			if (res == 1) {
				if(pare.isEmpty()) res = 1;
				else res = 0;
			}
			sb.append("#").append(test_case).append(" ").append(res);
			System.out.println(sb);
			
				
		}
	}
}
