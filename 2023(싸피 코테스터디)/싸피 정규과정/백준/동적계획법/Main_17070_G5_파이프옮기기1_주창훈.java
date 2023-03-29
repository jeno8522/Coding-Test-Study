package com.ssafy.dp;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main_17070_G5_파이프옮기기1_주창훈 {
	static int n;
	static int[][] graph;
	static int[][] visited;
	static int answer = 0;

	static void dfs(int r, int c, int dir) {
		if (r == n && c == n) {
			answer++;
			return;
		}
		switch (dir) {
		
		case 0: // 가로
			if (checkBoundary(r, c + 1) && graph[r][c + 1] != 1)
				dfs(r, c + 1, 0);
			if (checkBoundary(r + 1, c + 1) && graph[r + 1][c + 1] != 1 && checkWall(r, c))
				dfs(r + 1, c + 1, 2);
			break;
		case 1: // 세로
			if (checkBoundary(r + 1, c) && graph[r + 1][c] != 1)
				dfs(r + 1, c, 1);
			if (checkBoundary(r + 1, c + 1) && graph[r + 1][c + 1] != 1 && checkWall(r, c))
				dfs(r + 1, c + 1, 2);
			break;
		case 2: // 대각선
			if (checkBoundary(r, c + 1) && graph[r][c + 1] != 1)
				dfs(r, c + 1, 0);
			if (checkBoundary(r + 1, c) && graph[r + 1][c] != 1)
				dfs(r + 1, c, 1);
			if (checkBoundary(r + 1, c + 1) && graph[r + 1][c + 1] != 1 && checkWall(r, c))
				dfs(r + 1, c + 1, 2);
			break;

		default:
			break;
		}
	}

	static boolean checkBoundary(int r, int c) {
		return 1 <= r && r <= n && 1 <= c && c <= n;
	}
	static boolean checkWall(int r, int c) {	// 대각선 방향으로 갈 때 벽 check
		return graph[r][c + 1] == 0 && graph[r+1][c] == 0 && graph[r + 1][c + 1] == 0;
	}

	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		graph = new int[n + 1][n + 1];
		visited = new int[n + 1][n + 1];
		for (int i = 1; i <= n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= n; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		dfs(1, 2, 0);
		System.out.println(answer);
	}

}
