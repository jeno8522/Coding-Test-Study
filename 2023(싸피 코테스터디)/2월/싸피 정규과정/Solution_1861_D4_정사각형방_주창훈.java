package com.ssafy.combination;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_1861_D4_정사각형방_주창훈 {
	static int N;
	static int[][] graph;
	static boolean[][] visited;
	static int maxValue = Integer.MIN_VALUE;
	static int minPos = Integer.MAX_VALUE;
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };
	
	static void dfs(int r, int c, int cnt) {
		visited[r][c] = true;
		if (cnt > maxValue) {
			maxValue = cnt;
		}
		

		for (int i = 0; i < 4; i++) {
			int nr = r + dr[i];
			int nc = c + dc[i];
			if (nr >= 1 && nr <= N && nc >= 1 && nc <= N) {
				if (graph[nr][nc] == graph[r][c] + 1 && !visited[nr][nc]) {
					dfs(nr, nc, cnt + 1);
				}
			}
		}
	}

	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		for (int test_case = 1; test_case <= T; test_case++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			graph = new int[N + 1][N + 1];
			maxValue = Integer.MIN_VALUE;
			minPos = Integer.MAX_VALUE;
			for (int i = 1; i <= N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 1; j <= N; j++) {
					graph[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			int save = Integer.MIN_VALUE;
			for (int i = 1; i <= N; i++) {
				for (int j = 1; j <= N; j++) {
					visited = new boolean[N + 1][N + 1];
					maxValue = Integer.MIN_VALUE;
					dfs(i, j, 1);
					if(maxValue > save) {
						save = maxValue;
						minPos = graph[i][j];
					}
					else if(maxValue == save) {
						minPos = Math.min(minPos, graph[i][j]);
					}


				}
			}

			System.out.println("#" + test_case + " " + minPos + " " + save);
		}

	}

}
