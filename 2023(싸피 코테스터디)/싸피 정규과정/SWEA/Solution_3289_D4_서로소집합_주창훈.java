package s0227;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_3289_D4_서로소집합_주창훈 {
	static int N, M;
	static int[] parents;

	public static void makeSet(int v) {
		parents[v] = v;
	}

	public static int findSet(int v) {
		if (v == parents[v])
			return v;
		return parents[v] = findSet(parents[v]);
	}

	public static void union(int u, int v) {
		parents[findSet(u)] = findSet(v);
	}

	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		for (int test_case = 1; test_case <= T; test_case++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			parents = new int[N + 1];
			for (int i = 1; i <= N; i++) {
				makeSet(i);
			}
			System.out.print("#" + test_case + " ");
			for (int i = 0; i < M; i++) {
				st = new StringTokenizer(br.readLine());
				int mode = Integer.parseInt(st.nextToken());
				int root1 = Integer.parseInt(st.nextToken());
				int root2 = Integer.parseInt(st.nextToken());
				if (mode == 0)
					union(root1, root2);
				else {
					if (findSet(root1) == findSet(root2)) {
						System.out.print(1);
					} else {
						System.out.print(0);
					}
				}
			}
			System.out.println();
		}
	}

}
