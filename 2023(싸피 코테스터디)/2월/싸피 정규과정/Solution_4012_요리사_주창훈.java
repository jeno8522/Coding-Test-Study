package com.ssafy.divideconquer;

import java.awt.List;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution_4012_요리사_주창훈 {
	static int T;
	static int N;
	static int[][] graph;
	static int minValue = Integer.MAX_VALUE;
	static boolean[] visited;
	static int sumAll = 0;

	public static void comb(int cnt, int start) {
		if (cnt == N / 2) {
			check();
			return;
		}
		for (int i = start; i < N; i++) {
			visited[i] = true;
			comb(cnt + 1, i + 1);
			visited[i] = false;
		}
	}

	public static void check() {
		int taste1 = 0, taste2 = 0, result = 0;

		for (int i = 0; i < N - 1; i++) {
			for (int j = i + 1; j < N; j++) {
				if (visited[i] && visited[j]) {
					taste1 += graph[i][j] + graph[j][i];
				} else if (!visited[i] && !visited[j]) {
					taste2 += graph[i][j] + graph[j][i];
				}
			}
		}
		minValue = Math.min(minValue, Math.abs(taste1 - taste2));
	}

	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		T = Integer.parseInt(st.nextToken());
		for (int test_case = 1; test_case <= T; test_case++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			graph = new int[N][N];
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					graph[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			visited = new boolean[N];
			sumAll = 0;
			minValue = Integer.MAX_VALUE;
			comb(0, 0);
			System.out.print("#" + test_case + " ");
			System.out.println(minValue);
		}

	}

}
