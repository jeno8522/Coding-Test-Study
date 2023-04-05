package s0403;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main_3055_G4_탈출_주창훈 {
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };
	static int R, C;
	static char[][] graph;
	static int startR, startC;
	static int endR, endC;
	static ArrayDeque<int[]> water;
	static ArrayDeque<int[]> hog;

	static boolean checkBoundary(int r, int c) {
		return 0 <= r && r < R && 0 <= c && c < C;
	}

	static void floodBfs() {
		int waterCnt = water.size();
		boolean[][] visited = new boolean[R][C];
		for (int i = 0; i < waterCnt; i++) {
			int[] now = water.pollFirst();
			int r = now[0];
			int c = now[1];
			visited[r][c] = true;
			for (int j = 0; j < 4; j++) {
				int nr = r + dr[j];
				int nc = c + dc[j];
				if (!checkBoundary(nr, nc))
					continue;
				if (visited[nr][nc])
					continue;
				if (graph[nr][nc] == '.') {
					graph[nr][nc] = '*';
					visited[nr][nc] = true;
					water.addLast(new int[] { nr, nc });
				}
			}
		}
	}

	static boolean hogBfs() {
		int hogCnt = hog.size();
		boolean[][] visited = new boolean[R][C];
		for (int i = 0; i < hogCnt; i++) {
			int[] now = hog.pollFirst();
			int r = now[0];
			int c = now[1];
			if (graph[r][c] == 'D')
				return true;
			visited[r][c] = true;
			for (int j = 0; j < 4; j++) {
				int nr = r + dr[j];
				int nc = c + dc[j];
				if (!checkBoundary(nr, nc))
					continue;
				if (visited[nr][nc])
					continue;
				if (graph[nr][nc] == '.' || graph[nr][nc] == 'D') {
					visited[nr][nc] = true;
					hog.addLast(new int[] { nr, nc });
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
		water = new ArrayDeque<>();
		hog = new ArrayDeque<>();
		for (int i = 0; i < R; i++) {
			String str = br.readLine();
			for (int j = 0; j < C; j++) {
				graph[i][j] = str.charAt(j);
				if (graph[i][j] == 'S') {
					hog.add(new int[] { i, j });
				} else if (graph[i][j] == '*') {
					water.add(new int[] { i, j });
				} else if (graph[i][j] == 'D') {
					endR = i;
					endC = j;
				}
			}

		}
		int time = 0;
		boolean isKAKTUS = false;
		while (true) {
			floodBfs();
			if (hogBfs())
				break;
			if (hog.isEmpty()) {
				isKAKTUS = true;
				break;
			}
			time++;
		}
		if (isKAKTUS) {
			System.out.println("KAKTUS");
		} else {
			System.out.println(time);
		}
	}

}
