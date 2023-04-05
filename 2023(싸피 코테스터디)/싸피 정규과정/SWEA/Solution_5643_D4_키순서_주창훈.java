package s0403;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Solution_5643_D4_키순서_주창훈 {
	static int N, M;
	static ArrayList<Integer>[] up;
	static ArrayList<Integer>[] down;
	static int[] info;
	
	static void bfs(ArrayList<Integer>[] graph) {
		for (int i = 1; i <= N; i++) {
			ArrayDeque<Integer> queue = new ArrayDeque<>();
			boolean [] visited = new boolean[N+1];
			queue.add(i);
			visited[i] = true;
			while(!queue.isEmpty()) {
				int now = queue.pollFirst();
				visited[now] = true;
				for (int next : graph[now]) {
					info[next] += 1;
					if(visited[next]) continue;
					queue.addLast(next);
				}
			}
		}
	}
	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			info = new int[N+1];
			up = new ArrayList[N+1];
			down = new ArrayList[N+1];
			for (int i = 1; i <= N; i++) {
				up[i] = new ArrayList<>();
				down[i] = new ArrayList<>();
			}
			st = new StringTokenizer(br.readLine());
			M = Integer.parseInt(st.nextToken());
			for (int i = 0; i < M; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				up[a].add(b);
				down[b].add(a);
			}
			Arrays.fill(info, 1);
			bfs(up);
			bfs(down);
			
			System.out.println(Arrays.toString(info));
//			System.out.println("#" + tc + " " + result);
		}
	}

}

//1 5 1 6 5 5
