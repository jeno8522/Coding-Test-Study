package s0307;

import java.io.*;
import java.util.*;

public class Main_17143_G1_낚시왕_주창훈 {
	static class Shark {
		int r;
		int c;
		int s;
		int d;
		int z;

		public Shark(int r, int c, int s, int d, int z) {
			this.r = r;
			this.c = c;
			this.s = s;
			this.d = d;
			this.z = z;
		}
	}
	
	static int R, C, M;
	static int result;
	static Shark[][] graph;
	static ArrayList<Shark> sharks = new ArrayList<>();
	static int[] dr = { 0, -1, 1, 0, 0 };
	static int[] dc = { 0, 0, 0, 1, -1 };
	
	static void fishing(int c) {
		for (int i = 1; i <= R; i++) {
			if (graph[i][c] != null) {
				Shark now = graph[i][c];
				graph[i][c] = null;
				result += now.z;
				sharks.remove(now);
				return;
			}
		}
	}

	static void moveShark() {
		for (int i = 0; i < sharks.size(); i++) {
			sharks.set(i, updateSharkPosition(sharks.get(i)));
		}
	}
	
	static Shark updateSharkPosition(Shark now) {
		int r = now.r;
		int c = now.c;
		int s = now.s;
		int d = now.d;
		int z = now.z;
		
		if (d == 1 || d == 2) {
			s = s % ((R - 1) * 2);
			while (s > 0) {
				if (r == 1) {
					d = 2;
				}
				if (r == R) {
					d = 1;
				}
				r += dr[d];
				s--;
			}
		}
		else {
			s = s % ((C - 1) * 2);
			while (s > 0) {
				if (c == 1) {
					d = 3;
				}
				if (c == C) {
					d = 4;
				}
				c += dc[d];
				s--;
			}
		}
		return new Shark(r,c,now.s,d,z);
	}

	static void drawShark() {
		graph = new Shark[R + 1][C + 1];
		int z = sharks.size();
		// 역방향으로 검사 -> remove 시 건너 뛸 수 있음
		for (int i = z - 1; i >= 0; i--) {
			Shark now = sharks.get(i);
			if (graph[now.r][now.c] == null) {
				graph[now.r][now.c] = now;
			}
			else {
				if (graph[now.r][now.c].z > now.z) {
					sharks.remove(now);
				} else {
					sharks.remove(graph[now.r][now.c]);
					graph[now.r][now.c] = now;
				}
			}
		}
	}

	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine(), " ");
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		graph = new Shark[R + 1][C + 1];

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int r = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			int s = Integer.parseInt(st.nextToken());
			int d = Integer.parseInt(st.nextToken());
			int z = Integer.parseInt(st.nextToken());

			Shark shark = new Shark(r, c, s, d, z);
			graph[r][c] = shark;
			sharks.add(shark);
		}

		for (int i = 1; i <= C; i++) {
			fishing(i);
			moveShark();
			drawShark();
		}

		System.out.println(result);
	}


}