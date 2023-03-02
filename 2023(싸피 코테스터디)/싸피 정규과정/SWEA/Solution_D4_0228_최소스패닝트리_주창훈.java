package s0228;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution_D4_0228_최소스패닝트리_주창훈 {
	static int V, E;
	static Edge[] edgeList;
	static int[] parents;
	static long result;
	
	static class Edge implements Comparable<Edge>{
		int from, to;
		int weight;
		
		public Edge(int from, int to, int weight) {
			super();
			this.from = from;
			this.to = to;
			this.weight = weight;
		}

		@Override
		public int compareTo(Edge o) {
			return Integer.compare(this.weight, o.weight);
		}
	}
	static void makeSet() {
		parents = new int[V + 1];
		for (int i = 1; i <= V; i++) {
			parents[i] = i;
		}
	}
	static int findSet(int v) {
		if(v == parents[v]) return v;
		return parents[v] = findSet(parents[v]); 
	}
	
	static boolean union(int v, int u) {
		int vRoot = findSet(v);
		int uRoot = findSet(u);
		if(vRoot == uRoot) return false;
		parents[uRoot] = vRoot;
		return true;
	}
	
	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		for (int test_case = 1; test_case <= T; test_case++) {
			result = 0;
			st = new StringTokenizer(br.readLine());
			V = Integer.parseInt(st.nextToken());
			E = Integer.parseInt(st.nextToken());
			edgeList = new Edge[E];
			for (int i = 0; i < E; i++) {
				st = new StringTokenizer(br.readLine());
				int from = Integer.parseInt(st.nextToken());
				int to = Integer.parseInt(st.nextToken());
				int weight = Integer.parseInt(st.nextToken());
				edgeList[i] = new Edge(from, to, weight);
			}
			Arrays.sort(edgeList);
			
			makeSet();
			int cnt = 0;
			for (Edge e : edgeList) {
				if(union(e.from, e.to)) {
					result += e.weight;
					if(++cnt == V-1)
						break;
				}
			}
			System.out.println("#" + test_case + " " +result);
		}
	}

}
