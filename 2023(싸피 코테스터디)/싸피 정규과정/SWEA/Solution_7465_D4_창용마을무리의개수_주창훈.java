package s0227;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Solution_7465_D4_창용마을무리의개수_주창훈 {
	static int N, M;
	static int[] parents;
	static HashSet<Integer> set;
	public static void makeSet(int v) {
		parents[v] = v;
	}
	
	public static int findSet(int v) {
		if(v == parents[v]) return v;
		return parents[v] = findSet(parents[v]);
	}
	
	public static void union(int v, int u) {
		parents[findSet(u)] = findSet(v);
	}
	
	public static void countSet() {
		for (int v : parents) {
			set.add(findSet(v));
		}
	}
	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		for (int test_case = 1; test_case <= T; test_case++) {
			set = new HashSet<>();
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			parents = new int[N + 1];
			for (int i = 1; i <= N; i++) {
				makeSet(i);
			}
			for (int i = 0; i < M; i++) {
				st = new StringTokenizer(br.readLine());
				int p1 = Integer.parseInt(st.nextToken());
				int p2 = Integer.parseInt(st.nextToken());
				union(p1, p2);
			}
			countSet();
			System.out.println("#" + test_case + " " + (set.size() - 1));		//0제외

		}
	}

}
