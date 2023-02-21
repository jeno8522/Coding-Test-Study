package com.ssafy.graph;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main_1260_S2_DFS와BFS_주창훈 {
	static int N;
	static int M;
	static int V;
	static int [][] graph;
	static boolean [] visited;
	static StringBuilder sb;
	
	static void bfs(int start) {
		Queue<Integer> queue = new LinkedList<Integer>();
		queue.offer(start);
		visited[start] = true;
		while(!queue.isEmpty()) {
			int now = queue.poll();
			sb.append(now).append(" ");
			for (int i = 1; i < N + 1; i++) {
				if(graph[now][i] == 1 && !visited[i]) {
					queue.offer(i);
					visited[i] = true;
				}
			}
		}
	}
	private static void dfs(int start) {	
		visited[start] = true;
		sb.append(start).append(" ");
		for (int i = 1; i < N + 1; i++) {
			if(graph[start][i] == 1 && !visited[i]) {
				dfs(i);	
			}
		}
	}
	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		sb = new StringBuilder();
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		V = Integer.parseInt(st.nextToken());
		graph = new int [N + 1][N + 1];
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			graph[start][end] = 1;
			graph[end][start] = 1;
		}
		visited = new boolean [N + 1];
		dfs(V);
		sb.append("\n");
		visited = new boolean [N + 1];
		bfs(V);
		System.out.print(sb);
	}

}
