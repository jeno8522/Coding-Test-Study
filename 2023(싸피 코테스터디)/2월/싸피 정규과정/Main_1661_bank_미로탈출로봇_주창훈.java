package com.ssafy.graph;

import java.awt.List;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main_1661_bank_미로탈출로봇_주창훈 {
	static int C;
	static int R;
	static int startC, startR;
	static int endC, endR;
	static char[][] graph;
	static int [][] visited;
	static int res = 0;
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };

	static class Position {
		int r;
		int c;
		int d;

		Position() {
		}

		Position(int r, int c, int d) {
			this.r = r;
			this.c = c;
			this.d = d;
		}
	}

	static void bfs(Position p) {
		Queue<Position> q = new LinkedList<Position>();
		visited[p.r][p.c] = 1;
		q.offer(p);
		while (!q.isEmpty()) {
			Position now = q.poll();
			if(now.r == endR && now.c == endC) {
				res = now.d;
				break;
			}
			for (int i = 0; i < 4; i++) {
				int nr = now.r + dr[i];
				int nc = now.c + dc[i];
				if ((0 <= nr && nr < R) && (0 <= nc && nc < C)) {
					if (graph[nr][nc] == '0' && visited[nr][nc] == 0) {
						visited[nr][nc] = 1;
						q.offer(new Position(nr, nc, now.d + 1));
					}
				}
			}
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		C = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());
		graph = new char[R][C];
		visited = new int[R][C];
		st = new StringTokenizer(br.readLine());
		startC = Integer.parseInt(st.nextToken());
		startR = Integer.parseInt(st.nextToken());
		endC = Integer.parseInt(st.nextToken());
		endR = Integer.parseInt(st.nextToken());
		
		startC -= 1;
		startR -= 1;
		endC -= 1;
		endR -= 1;

		for (int i = 0; i < R; i++) {
			graph[i] = br.readLine().toCharArray();
		}
		
		Position start = new Position(startR, startC, 0);
		bfs(start);
		System.out.println(res);

	}

}
