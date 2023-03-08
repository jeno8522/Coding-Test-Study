package com.ssafy.hw.step2;

import java.io.*;
import java.util.*;

public class Solution_2115_모의_벌꿀채취_주창훈 {
	static int N, M, C;
	static int[][] graph;
	static int[] workers;
	static int max;
	static int sumHoneyA, sumHoneyB;

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; ++tc) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			C = Integer.parseInt(st.nextToken());
			graph = new int[N][N];
			workers = new int[2];
			max = Integer.MIN_VALUE;
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine(), " ");
				for (int j = 0; j < N; ++j)
					graph[i][j] = Integer.parseInt(st.nextToken());
			}
			searchHoney(0, 0);
			sb.append("#").append(tc).append(" ").append(max).append("\n");
		}
		System.out.println(sb);
	}

	static void searchHoney(int cnt, int start) { // 2개 뽑는 조합
		if (cnt == 2) {	// 일꾼 두명
			if (workers[0] < workers[1] && workers[1] < workers[0] + M)	// 인덱스 겹치는 지 check
				return;
			if (workers[0] / N != (workers[0] + (M - 1)) / N)	// 채취한 시작과 끝이 같은 행인지 check
				return;
			if (workers[1] / N != (workers[1] + (M - 1)) / N)
				return;
			max = Math.max(max, getHoney(workers[0], workers[1]));
			return;
		}
		for (int i = start; i < N * N; i++) { // 전체 graph 칸 갯수 만큼
			workers[cnt] = i;
			searchHoney(cnt + 1, i + 1);
		}
	}

	private static int getHoney(int honeyA, int honeyB) {
		sumHoneyA = 0;
		for (int i = 1; i <= M; i++) {
			check(0, honeyA, honeyA + M, i, 0, 0, 0);
		}
		sumHoneyB = 0;
		for (int i = 1; i <= M; i++) {
			check(1, honeyB, honeyB + M, i, 0, 0, 0);
		}
		int honeySum = sumHoneyA + sumHoneyB;
		return honeySum;
	}

	static void check(int type, int start, int end, int now, int cnt, int sum, int rev) {
		if (cnt == now) {
			if (sum <= C) {
				if (type == 0)
					sumHoneyA = Math.max(sumHoneyA, rev);
				else
					sumHoneyB = Math.max(sumHoneyB, rev);
			}
			return;
		}
		for (int i = start; i < end; i++) {
			int val = graph[i / N][i % N];
			check(type, i + 1, end, now, cnt + 1, sum + val, rev + (int) Math.pow(val, 2));
		}
	}
}