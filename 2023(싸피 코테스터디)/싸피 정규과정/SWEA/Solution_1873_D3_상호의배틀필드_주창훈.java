import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution_1873_D3_상호의배틀필드_주창훈 {

	static StringBuilder sb = new StringBuilder();
	static char[][] map;
	static int H, W, px, py, nx, ny, position;
	static char[] pos = { '^', 'v', '<', '>' };
	static boolean flag;
	static int[] dx = { -1, 1, 0, 0 };
	static int[] dy = { 0, 0, -1, 1 };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			sb.append("#").append(tc).append(" ");
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			H = Integer.parseInt(st.nextToken());
			W = Integer.parseInt(st.nextToken());

			map = new char[H][W];

			String s = "";
			for (int i = 0; i < H; i++) {
				s = br.readLine();
				for (int j = 0; j < W; j++) {
					char ch = map[i][j] = s.charAt(j);
					if (ch == '^' || ch == 'v' || ch == '<' || ch == '>') {
						px = i;
						py = j;
						input(ch);
						map[i][j] = '.';
					}
				}
			}

			int len = Integer.parseInt(br.readLine());
			s = br.readLine();
			for (int i = 0; i < len; i++) {
				switch (s.charAt(i)) {
				case 'U':
					position = 0;
					nx = px + dx[0];
					ny = py + dy[0];
					if (MoveCheck(nx, ny) && map[nx][ny] == '.') {
						px = nx;
						py = ny;
					}
					break;
				case 'D':
					position = 1;
					nx = px + dx[1];
					ny = py + dy[1];
					if (MoveCheck(nx, ny) && map[nx][ny] == '.') {
						px = nx;
						py = ny;
					}
					break;
				case 'L':
					position = 2;
					nx = px + dx[2];
					ny = py + dy[2];
					if (MoveCheck(nx, ny) && map[nx][ny] == '.') {
						px = nx;
						py = ny;
					}
					break;
				case 'R':
					position = 3;
					nx = px + dx[3];
					ny = py + dy[3];
					if (MoveCheck(nx, ny) && map[nx][ny] == '.') {
						px = nx;
						py = ny;
					}
					break;
				case 'S':
					nx = px + dx[position];
					ny = py + dy[position];
					while (Game(nx, ny)) {
						nx += dx[position];
						ny += dy[position];
					}
					break;
				}
			}
			map[px][py] = pos[position];
			for (int i = 0; i < H; i++) {
				for (int j = 0; j < W; j++) {
					sb.append(map[i][j]);
				}
				sb.append("\n");
			}
		}
		System.out.println(sb.toString());
	}

	private static void input(char ch) {
		switch (ch) {
		case '^':
			position = 0;
			break;
		case 'v':
			position = 1;
			break;
		case '<':
			position = 2;
			break;
		case '>':
			position = 3;
			break;
		}
	}

	public static boolean Game(int x, int y) {
		if (!MoveCheck(x, y))
			return false;
		switch (map[x][y]) {
		case '.':
			return true;
		case '*':
			map[x][y] = '.';
			return false;
		case '#':
			return false;
		case '-':
			return true;
		}
		return false;
	}

	public static boolean MoveCheck(int x, int y) {
		if (x < 0 || x >= H || y < 0 || y >= W)
			return false;
		return true;
	}
}