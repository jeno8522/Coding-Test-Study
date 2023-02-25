package com.ssafy.algorithm;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class Solution_1210_D4_Ladder1_주창훈 {
	public static int[] dr = { 0, 0, -1 };
	public static int[] dc = { -1, 1, 0 };
	public static int[][] graph = new int[100][100];
	public static boolean[][] visited;
	public static int result;

	public static void moveToCeil(int r, int c) {
//		visited = new boolean[100][100];
//		visited[99][99] = true;
		while (true) {
			if (r == 0) {
				result = c;
				break;
			}
			for (int i = 0; i < 3; i++) {
				int nr = r + dr[i];
				int nc = c + dc[i];
				if (isValidPosition(nr, nc) && (graph[nr][nc] == 1)) {
					{
						graph[r][c] = 0;
						r = nr;
						c = nc;
					}
				}
			}
		}
	}

	public static boolean isValidPosition(int r, int c) {
		return (r >= 0 && r < 100) && (c >= 0 && c < 100);
	}

	public static void main(String args[]) throws Exception {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int T = 10;
		int goalPosX = 0;
		int goalPosY = 0;

		for (int test_case = 1; test_case <= T; test_case++) {
			int testNum = Integer.parseInt(in.readLine());
			for (int i = 0; i < 100; i++) {
				StringTokenizer st = new StringTokenizer(in.readLine(), " ");
				for (int j = 0; j < 100; j++) {
					graph[i][j] = Integer.parseInt(st.nextToken());
					if(graph[i][j] == 2) {
						goalPosX = i;
						goalPosY = j;
					}
				}
			}
			moveToCeil(goalPosX, goalPosY);
			System.out.println("#" + testNum + " " + result);
		}
	}
}