package s0224;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_10026_G5_적록색약_주창훈 {
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };
	static int N;
	static char[][] graph;
	static boolean[][] visited;
	static int res = 0;
	static int resRGB = 0;
	
	static void dfs(int r, int c, char color) {
		visited[r][c] = true;
		for (int i = 0; i < 4; i++) {
			int nr = r + dr[i];
			int nc = c + dc[i];
			if(checkBoundary(nr, nc) && !visited[nr][nc]) {
				if(color == graph[nr][nc]) {
					dfs(nr,nc,color);
				}
			}
		}
	}
	
	
	
	static void dfsRGB(int r, int c, char color) {
		visited[r][c] = true;
		for (int i = 0; i < 4; i++) {
			int nr = r + dr[i];
			int nc = c + dc[i];
			if(checkBoundary(nr, nc) && !visited[nr][nc]) {
				if(color == graph[nr][nc] || checkRGB(color, graph[nr][nc])) {
					dfsRGB(nr,nc,color);
				}
			}
		}
	}

	static boolean checkBoundary(int r, int c) {
		return r >= 0 && r < N && c >= 0 && c < N;
	}
	
	static boolean checkRGB(char color1, char color2) {
		if(color1 == 'R' && color2 =='G' ) return true;
		else if(color1 == 'G' && color2 =='R') return true;
		return false;
	}

	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		graph = new char[N][N];
		visited = new boolean[N][N];
		for (int i = 0; i < N; i++) {
			String str = br.readLine();
			graph[i] = str.toCharArray();
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if(!visited[i][j]) {
					dfs(i,j,graph[i][j]);
					res++;
				}
			}
		}
		visited = new boolean[N][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if(!visited[i][j]) {
					dfsRGB(i,j,graph[i][j]);
					resRGB++;
				}
			}
		}
		System.out.println(res + " " + resRGB);

	}

}
