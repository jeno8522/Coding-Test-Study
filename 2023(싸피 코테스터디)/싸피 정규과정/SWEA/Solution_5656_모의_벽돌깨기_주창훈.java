package com.ssafy.hw.step2;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Solution_5656_모의_벽돌깨기_주창훈 {
	static BufferedReader br;
	static StringTokenizer st;
	static int[][] graph, graphSave;
	static int[] dx = { 0, -1, 0, 1 };
	static int[] dy = { -1, 0, 1, 0 };
	static int[] marblePos;
	static boolean[] visited;
	static int N, W, H;
	static int result = Integer.MAX_VALUE;

	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("res/input.txt"));
		br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int test_case = 1; test_case <= T; test_case++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			W = Integer.parseInt(st.nextToken());
			H = Integer.parseInt(st.nextToken());
			graph = new int[H][W];
			graphSave = new int[H][W];
			marblePos = new int[N];
			visited = new boolean[W];

			result = Integer.MAX_VALUE;
			for (int i = 0; i < H; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < W; j++) {
					int value = Integer.parseInt(st.nextToken());
					graph[i][j] = value;
					graphSave[i][j] = value;
				}
			}

			permutation(0);
			System.out.println("#" + test_case + " " + result);
		}
	}

	private static void permutation(int cnt) { // 중복 순열
		if (cnt == N) { 
			throwMarble();
			result = Math.min(result, countBricks());	// 매 결과 마다 남은 벽돌 갯수의 최솟값 갱신
			recoverGraph();								// 그래프 원상복구
			return;
		}
		for (int i = 0; i < W; i++) {
			marblePos[cnt] = i;
			permutation(cnt + 1);
		}
	}

	private static void throwMarble() {
		for (int i = 0; i < N; i++) {
			int start = marblePos[i];	// 마블 떨어트릴 위치
			for (int j = 0; j < H; j++) {
				if (graph[j][start] > 0) {	// 벽돌이 존재하면 break
					shotBrick(j, start); // 구슬 떨어뜨리기
					moveBricks(); // 벽돌들 아래로 떨어뜨리기
					break;
				}
			}
			
		}
	}

	private static void shotBrick(int r, int c) {
		Deque<int[]> deque = new ArrayDeque<>();
		deque.add(new int[] { r, c, graph[r][c] });
		graph[r][c] = 0;	// 중심부 0으로 변경
		int nr, nc;

		while (!deque.isEmpty()) {
			int[] now = deque.poll(); // 깨진 벽돌 꺼내기
			int area = now[2];		// 벽돌 깰 area

			for (int d = 1; d < area; d++) { // area 만큼
				for (int i = 0; i < 4; i++) {
					nr = now[0] + dx[i] * d;	// area 만큼 곱한 범위 
					nc = now[1] + dy[i] * d;
					if (!checkBoundary(nr, nc) || graph[nr][nc] == 0) //경계 체크, 벽돌없으면 continue
						continue;
					if (graph[nr][nc] > 0) {	// 벽돌이 존재하면 덱에 넣어주고
						deque.add(new int[] { nr, nc, graph[nr][nc] });
						graph[nr][nc] = 0; // 벽돌을 0으로 변경
						continue;
					}
				}
			}
		}
	}

	private static void moveBricks() {
		Deque<Integer> deque = new ArrayDeque<Integer>();
		for (int j = 0; j < W; j++) {
			for (int i = 0; i < H; i++) {
				if (graph[i][j] > 0) {		// 남은 벽돌들 덱에 넣어줌
					deque.add(graph[i][j]);
				}
			}
			for (int i = H - 1; i >= 0; i--) {
				if (deque.isEmpty()) {	// 남은 벽돌들 다 뺐으면 나머지는 0으로 채워줌
					graph[i][j] = 0;
				} else {
					graph[i][j] = deque.pollLast();	// 덱에 넣어준 벽돌들을 graph에 채워줌
				}
			}
		}
	}

	private static int countBricks() {
		int cnt = 0;
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				if (graph[i][j] > 0)
					cnt++;
			}
		}
		return cnt;
	}

	private static void recoverGraph() {
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				graph[i][j] = graphSave[i][j];
			}
		}
	}

	private static boolean checkBoundary(int r, int c) {
		return r >= 0 && r < H && c >= 0 && c < W;
	}
}