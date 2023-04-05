package s0405;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_4014_모의_활주로건설_주창훈 {
	static int N, X;
	static int[][] map;
	static int[][] rotateMap;
	static int[][] visited;
	static int result = 0;

	static void checkLine(int[][] graph) {
		visited = new int[N][N]; // 1이면 단순 방문, 2면 경사로 설치
		for (int i = 0; i < N; i++) {
			int h = graph[i][0]; // 첫번째 높이로 h 초기화
			visited[i][0] = 1; // 단순 방문 체크
			boolean isValid = true;
			for (int j = 1; j < N; j++) {
				if (visited[i][j] != 0) // 방문했거나 경사로를 설치해놨으면 continue
					continue;
				visited[i][j] = 1; // 일단 단순 방문 체크
				if (h != graph[i][j]) {	// 높이가 달라지면 박스 설치
					if (!canPutBox(graph, h, graph[i][j], i, j)) {	// 박스 하나라도 설치 실패하면 활주로 건설실패, 다음 라인으로
						isValid = false;
						break;
					}
					h = graph[i][j]; // 달라진 높이로 h 갱신해줌
				}
			}
			if (isValid) {
				result++;
			}
		}
	}

	static boolean canPutBox(int[][] graph, int prev, int now, int nowR, int nowC) {
		int prevR = nowR;
		int prevC = nowC - 1;
		if (prev + 1 == now) {
			if (!checkBoundary(prevR, prevC - X + 1)) // 박스가 범위 밖이면 return false
				return false;
			for (int i = 1; i < X; i++) {
				if (graph[prevR][prevC - i] != prev) // 박스 놓일 자리가 높이가 일정하지 않으면 return false
					return false;
				if (visited[prevR][prevC - i] == 2) // 박스 놓일 자리에 이미 박스가 놓여져 있다면 return false
					return false;
			}
			for (int i = 0; i < X; i++) {
				visited[prevR][prevC - i] = 2; // 경사로 설치
			}
			return true;
		} else if (prev - 1 == now) {
			if (!checkBoundary(nowR, nowC + X - 1)) // 박스가 범위 밖이면 return false
				return false;
			for (int i = 1; i < X; i++) {
				if (graph[nowR][nowC + i] != now) // 박스 놓일 자리가 높이가 일정하지 않으면 return false
					return false;
				if (visited[nowR][nowC + i] == 2) // 박스 놓일 자리에 이미 박스가 놓여져 있다면 return false
					return false;
			}
			for (int i = 0; i < X; i++) {
				visited[nowR][nowC + i] = 2; // 경사로 설치
			}
			return true;
		}
		return false;
	}

	static boolean checkBoundary(int r, int c) {
		return 0 <= r && r < N && 0 <= c && c < N;
	}

	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			X = Integer.parseInt(st.nextToken());
			map = new int[N][N];
			rotateMap = new int[N][N];
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					rotateMap[i][j] = map[N - 1 - j][i];
				}
			}
			result = 0;
			checkLine(map);
			checkLine(rotateMap);
			System.out.println("#" + tc + " " + result);
		}
	}
}