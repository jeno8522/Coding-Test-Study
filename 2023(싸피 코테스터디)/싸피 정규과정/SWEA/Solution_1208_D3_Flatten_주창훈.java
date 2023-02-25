package com.ssafy.recursive;
import java.util.Arrays;
import java.util.Scanner;
import java.io.FileInputStream;

class Solution_1208_D3_Flatten_주창훈 {
	static int [] boxes;
	static int res;
	public static void main(String args[]) throws Exception {

//		System.setIn(new FileInputStream("res/input.txt"));

		Scanner sc = new Scanner(System.in);
		int T = 10;
		


		for (int test_case = 1; test_case <= T; test_case++) {
			int cnt = sc.nextInt();
			int right = 99;
			int left = 0;
			boxes = new int[100];
			for (int i = 0; i < 100; i++) {
				boxes[i] = sc.nextInt();
			}
			
			
			for (int i = 0; i < cnt; i++) {
				Arrays.sort(boxes);
				boxes[left] += 1;
				boxes[right] -= 1;
				
			}
			Arrays.sort(boxes);
			res = boxes[right] - boxes[left];
			System.out.println("#" + test_case + " " + res);
		}
	}
}


