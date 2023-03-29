package com.ssafy.dp;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_1600_G3_말이되고픈원숭이_주창훈 {
	static int[] h_dr = { 1, 2, 2, 1, -1, -2, -2, -1 };
	static int[] h_dc = { 2, 1, -1, -2, -2, -1, 1, 2 };
	static int[] m_dr = { 1, 0, -1, 0 };
	static int[] m_dc = { 0, 1, 0, -1 };

	static int k, w, h;
	static int[][] graph;
	static int[][][] visited;
	

	static boolean checkBoundary(int r, int c) {
		return r >= 0 && r < h && c >= 0 && c < w;
	}

	static void bfs(int startR, int startC) {
		ArrayDeque<int[]> q = new ArrayDeque<>();
		q.addLast(new int[] { startR, startC, 0, 0 });
		while (!q.isEmpty()) {
			int[] now = q.pollFirst();
			int r = now[0];
			int c = now[1];
			int cnt = now[2];
			int chance = now[3];
			visited[r][c][chance] = Math.min(visited[r][c][chance], cnt);
			for (int i = 0; i < 4; i++) {
				int nr = r + m_dr[i];
				int nc = c + m_dc[i];
				if (!checkBoundary(nr, nc))
					continue;
				if (cnt + 1 >= visited[nr][nc][chance])
//				if(cnt+1 >= minCnt)
					continue;
				if (graph[nr][nc] == 1)
					continue;
				q.addLast(new int[] { nr, nc, cnt + 1, chance });
				visited[nr][nc][chance] = cnt + 1;
			}
			if (chance == k)
				continue;
			for (int i = 0; i < 8; i++) {
				int nr = r + h_dr[i];
				int nc = c + h_dc[i];
				if (!checkBoundary(nr, nc))
					continue;
				if (cnt + 1 >= visited[nr][nc][chance+1])
//				if(cnt+1 >= minCnt)
					continue;
				if (graph[nr][nc] == 1)
					continue;
				q.addLast(new int[] { nr, nc, cnt + 1, chance + 1 });
				visited[nr][nc][chance+1] = cnt + 1;
			}
		}
	}

	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		k = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		w = Integer.parseInt(st.nextToken());
		h = Integer.parseInt(st.nextToken());
		graph = new int[h][w];
		visited = new int[h][w][k + 1];
		for (int i = 0; i < h; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < w; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				for (int a = 0; a <= k; a++) {
					visited[i][j][a] = Integer.MAX_VALUE;
				}
			}
		}

		bfs(0, 0);
		
		
		int minCnt = Integer.MAX_VALUE;
		for (int i = 0; i <= k; i++) {
			minCnt = Math.min(minCnt, visited[h-1][w-1][i]);
		}
		if (minCnt == Integer.MAX_VALUE) {
			System.out.println(-1);
		} else {
			System.out.println(minCnt);
		}
	}

}
