package homework;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Solution_1954_D2_달팽이숫자_주창훈 {
	static int[] dr = { 0, 1, 0, -1 };	// 방향 벡터
	static int[] dc = { 1, 0, -1, 0 };
	static int[][] graph;
	static boolean[][] visited;	// 방문 체크
	static int cnt = 1;
	static int n;

	static void dfs() {
		int r = 0;
		int c = 0;
		int dIdx = 0;	// 현재 방향
		
		while (cnt <= n * n) {	// while은 n제곱만큼 돈다
			graph[r][c] = cnt++;
			visited[r][c] = true;

			r += dr[dIdx];
			c += dc[dIdx];

			if (!isValid(r, c)) {	// 다음 번호가 들어갈 자리가 아니면
				r -= dr[dIdx];		// r, c 원상복귀
				c -= dc[dIdx];
				dIdx++;				// 다음 방향벡터로 설정 후
				dIdx %= 4;
				r += dr[dIdx];		// 다음 번호가 들어갈 자리 설정
				c += dc[dIdx];
			}
		}
	}

	static boolean isValid(int r, int c) {		// 현재 좌표가 다음 번호가 들어갈 자리인지 체크하는 함수
		if (0 <= r && r < n && 0 <= c && c < n) {		// 경계 확인
			if (graph[r][c] == 0 && !visited[r][c]) {	// visited 확인

				return true;
			}
		}
		return false;

	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		StringBuilder sb;
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int T;
		T = Integer.parseInt(bf.readLine());

		for (int test_case = 1; test_case <= T; test_case++) {
			n = Integer.parseInt(bf.readLine());
			graph = new int[n][n];
			visited = new boolean[n][n];
			cnt = 1;
			dfs();
			sb = new StringBuilder();
			sb.append("#").append(test_case).append(" ").append("\n");
			for (int[] line : graph) {
				for (int e : line) {
					sb.append(e).append(" ");
				}
				sb.append("\n");
			}
			System.out.print(sb.toString());
		}
	}
}