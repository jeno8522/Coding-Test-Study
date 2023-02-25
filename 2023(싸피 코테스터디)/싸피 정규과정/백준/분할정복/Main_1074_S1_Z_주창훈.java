package com.ssafy.divideconquer;

import java.util.Arrays;
import java.util.Scanner;

public class Main_1074_S1_Z_주창훈 {
	static int N;
	static int R, C;
	static int cnt = 0;
	static int res;

	public static void search(int r, int c, int size) {
		if (r == R && c == C) {
			System.out.println(cnt);
			System.exit(0);
		}
		if (size >= 2) {
			if (r + size > R && c + size > C) {
				
				int half = size / 2;
				search(r, c, half);
				search(r, c + half, half);
				search(r + half, c, half);
				search(r + half, c + half, half);
			}
			else {
				cnt += size * size;
			}
		}
		else {
			cnt++;
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		R = sc.nextInt();
		C = sc.nextInt();
		N = (int) Math.pow(2, N);
		search(0, 0, N);
	}

}
