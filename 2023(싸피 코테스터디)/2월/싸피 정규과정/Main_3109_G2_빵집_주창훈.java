package com.ssafy.backtracking;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_3109_G2_빵집_주창훈 {
	static int[] dr = { -1, 0, 1 };
	static int[] dc = { 1, 1, 1 };
	static char[][] graph;
	static int R;
	static int C;
	static int res = 0;

	public static boolean makePipeline(int startR, int startC) {
		if (startC == C - 1) {
			res += 1;
			return true;
		}
		for (int i = 0; i < 3; i++) {
			int nr = startR + dr[i];
			int nc = startC + dc[i];
			if (nr >= 0 && nr < R && nc >= 0 && nc < C) {
				if (graph[nr][nc] == '.') {
					graph[nr][nc] = 'X';
					if(makePipeline(nr, nc))
						return true;
				}
			}	
		}
		return false;
	}

	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		graph = new char[R][C];
		for (int i = 0; i < R; i++) {
			graph[i] = br.readLine().toCharArray();
		}
		for (int i = 0; i < R; i++) {
			makePipeline(i, 0);
		}
		System.out.println(res);

	}

}
