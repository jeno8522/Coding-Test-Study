package com.ssafy.temporary;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main_7576_G5_토마토_주창훈 {
	static int N, M;
	static int[][] graph;
	static Deque<int[]> q = new ArrayDeque<int[]>();
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };
	static int res;

	public static void bfs() {
		int[] now = new int[3];
		while (!q.isEmpty()) {
			now = q.pollFirst();
			int r = now[0];
			int c = now[1];
			int cnt = now[2];
			res = Math.max(res, cnt);
			for (int i = 0; i < 4; i++) {
				int nr = r + dr[i];
				int nc = c + dc[i];
				if (nr >= 0 && nr < N && nc >= 0 && nc < M) {
					if (graph[nr][nc] == 0) {
						graph[nr][nc] = 1;
						int[] next = new int[3];
						next[0] = nr;
						next[1] = nc;
						next[2] = cnt + 1;
						q.addLast(next);
					}
				}

			}
		}
	}

	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		M = Integer.parseInt(st.nextToken());
		N = Integer.parseInt(st.nextToken());
		graph = new int[N][M];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
				if (graph[i][j] == 1) {
					int[] tmp = new int[3];
					tmp[0] = i;
					tmp[1] = j;
					tmp[2] = 0;
					q.addLast(tmp);
				}
			}
		}
		bfs();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (graph[i][j] == 0) {
					System.out.println(-1);
					System.exit(0);
				}
			}
		}
		System.out.println(res);
	}

}
