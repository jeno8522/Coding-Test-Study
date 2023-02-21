package com.ssafy.backtracking;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_1992_S1_쿼드트리_주창훈 {
	static int N;
	static int[][] graph;
	static String res = "";
	public static void quadTree(int r, int c, int size) {
		int check_res = check(r,c,size);
		if(check_res != -1) {
			res += Integer.toString(check_res);
			return;
		}
		else {
			int half = size / 2;
			res += "(";
			quadTree(r, c, half);
			quadTree(r, c + half, half);
			quadTree(r + half, c, half);
			quadTree(r + half, c + half, half);
			res += ")";
			
		}
	}
	public static int check(int r, int c, int size) {
		int color = graph[r][c];
		for (int i = r; i < r + size; i++) {
			for (int j = c; j < c+ size; j++) {
				if(graph[i][j] != color) {
					return -1;
				}
			}
		}
		return color;
	}
	
	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		graph = new int[N][N];
		for (int i = 0; i < N; i++) {
			String str = br.readLine();
			for (int j = 0; j < N; j++) {
				graph[i][j] = Character.getNumericValue(str.charAt(j));
			}
		}
		quadTree(0, 0, N);
		System.out.println(res);
	}

}
