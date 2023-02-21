package com.ssafy.backtracking;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main_1987_G4_알파벳_주창훈 {
	static int R;
	static int C;
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };
	static int[][] graph;
	static boolean[] visited = new boolean[26];
	static int answer = Integer.MIN_VALUE;

	public static void dfs(int x, int y, int cnt) {
		if (visited[graph[x][y]]) {
			answer = Math.max(answer, cnt);
			return;
		} else {
			visited[graph[x][y]] = true;
			for (int i = 0; i < 4; i++) {
				int nr = x + dr[i];
				int nc = y + dc[i];
				if (0 <= nr && nr < R && 0 <= nc && nc < C) {
					dfs(nr, nc, cnt + 1);
				}
			}
			visited[graph[x][y]] = false;
		}
	}

	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		graph = new int[R][C];
		for (int i = 0; i < R; i++) {
			String tmp = br.readLine();
			for (int j = 0; j < C; j++) {
				graph[i][j] = tmp.charAt(j) - 'A';
			}
		}
		dfs(0, 0, 0);
		System.out.println(answer);
	}

}
