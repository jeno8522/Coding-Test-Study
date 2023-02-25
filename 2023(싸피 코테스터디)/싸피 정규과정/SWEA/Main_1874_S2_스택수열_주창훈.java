package com.ssafy.hw.step2;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main_1874_S2_스택수열_주창훈 {
	static Deque<Integer> stack = new ArrayDeque<>();
	static Deque<Integer> l = new ArrayDeque<>();
	static ArrayList<Integer> seq = new ArrayList<>();
	static boolean isSuccess = true;
	static int N;
	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		N = Integer.parseInt(st.nextToken());
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			seq.add(Integer.parseInt(st.nextToken()));
			l.offerLast(i+1);
		}
		
		for (int i = 0; i < N; i++) {
			if(!isSuccess) break;
			int num = seq.get(i);
			if(stack.isEmpty() || stack.peekLast() < num) {
				while(true) {
					if(l.isEmpty()) {
						isSuccess = false;
						break;
					}
					int tmp = l.pollFirst();
					stack.addLast(tmp);
					sb.append("+").append("\n");
					if(tmp == num) {
						stack.pollLast();
						sb.append("-").append("\n");
						break;
					}
				}
					
			}
			else if(stack.peekLast() >= num) {
				while(true) {
					if(stack.isEmpty()) {
						isSuccess = false;
						break;
					}
					int tmp = stack.pollLast();
					sb.append("-").append("\n");
					if(tmp == num) break;
				}
			}
		}
		if(isSuccess) {
			System.out.print(sb);
		}
		else {
			System.out.println("NO");
		}
	}

}
