package com.ssafy.hw.step2;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution_1949_모의_등산로조성_주창훈 {
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };
	static int[][] graph;
	static boolean[][] visited;
	static int N;
	static int K;
	static ArrayList<int[]> maxPos;
	static int maxValue = Integer.MIN_VALUE;
	static int res = Integer.MIN_VALUE;

	public static void dfs(int r, int c, int cnt, boolean isCut) {
		res = Math.max(res, cnt);
		for (int i = 0; i < 4; i++) {
			int nr = r + dr[i];
			int nc = c + dc[i];
			if (checkBoundary(nr, nc) && !visited[nr][nc]) {
				if (graph[r][c] > graph[nr][nc]) {	// 다음 높이가 더 낮은 경우
					visited[nr][nc] = true;
					dfs(nr, nc, cnt + 1, isCut);
					visited[nr][nc] = false;
				} else if (!isCut && graph[r][c] > graph[nr][nc] - K) {			//현재높이 > 다음높이 - K 이고 기회 안썼으면
					visited[nr][nc] = true;
					int tmp = graph[nr][nc];
					graph[nr][nc] = graph[r][c] - 1;
					dfs(nr, nc, cnt + 1, true);
					graph[nr][nc] = tmp;
					visited[nr][nc] = false;
				}
			}
		}
	}

	public static boolean checkBoundary(int r, int c) {
		return (r >= 0 && r < N) && (c >= 0 && c < N);
	}

	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		for (int test_case = 1; test_case <= T; test_case++) {
			st = new StringTokenizer(br.readLine());
			maxValue = Integer.MIN_VALUE;
			res = Integer.MIN_VALUE;
			N = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());
			graph = new int[N][N];
			visited = new boolean[N][N];
			maxPos = new ArrayList<>();
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					graph[i][j] = Integer.parseInt(st.nextToken());
					maxValue = Math.max(maxValue, graph[i][j]);
				}
			}

			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (maxValue == graph[i][j]) {
						maxPos.add(new int[] { i, j });
					}
				}
			}
			for (int i = 0; i < maxPos.size(); i++) {
				visited[maxPos.get(i)[0]][maxPos.get(i)[1]] = true;
				dfs(maxPos.get(i)[0], maxPos.get(i)[1], 1, false);
				visited[maxPos.get(i)[0]][maxPos.get(i)[1]] = false;
			}
			System.out.println("#" + test_case + " " + res);
		}
	}

}