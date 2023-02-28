package s0228;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

import s0228.MSTKRUSKAL.Edge;

/**
 * 시간 복잡도 O(V^3)
 * 
 */

public class MST_PRIM_PQ {
	static class Edge implements Comparable<Edge> {
		int from, to, weight;

		public Edge(int from, int to, int weight) {
			super();
			this.from = from;
			this.to = to;
			this.weight = weight;
		}

		@Override
		public int compareTo(Edge o) {
			// TODO Auto-generated method stub
			return Integer.compare(this.weight, o.weight);
		}
	}
	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		// 데이터 입력 받기
		int N = Integer.parseInt(st.nextToken());
		int E = Integer.parseInt(st.nextToken());
		
		// 각 정점 별로 인접 리스트
		ArrayList<Edge>[] adj = new ArrayList[N];
		for (int i = 0; i < N; i++) {
			adj[i] = new ArrayList<>();
		}
		boolean[] visited = new boolean[N]; // 노드의 방문 처리

		for (int i = 0; i < E; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			int weight = Integer.parseInt(st.nextToken());
			adj[from].add(new Edge(from, to, weight));
			adj[to].add(new Edge(to, from, weight));
		}
		
		// 선택된 정점 집합에서 갈 수 있는 모든 Edge를 저장할 PQ
		PriorityQueue<Edge> queue = new PriorityQueue<>();
		
		int cnt = 1;	// 선택 된 정점의 수를 count
		int result = 0; // MST 값

		// 선택된 임의의 정점에서 갈 수 있는 모든 정점의 Edge를 PQ에 담기
		queue.addAll(adj[0]);	// 선택한 0번 정점의 모든 Edge를 저장
		visited[0] = true;		// 0번 정점을 방문 체크

		// 모든 정점을 반복 하면서
		while(cnt != N) {
			
			// 갈 수 있는 정점이 edge 중 최소 edge를 추출
			Edge min = queue.poll();
			if(visited[min.to]) {	//이미 가본 정점이라면  pass
				continue;
			}
			// 최소 비용의 노드를 찾았다면 해당 노드 방문 표시 하고, 선택한 노드 처리, 최솟값 갱신
			result += min.weight; // 선택된 최소 비용을 누적해 주기
			// 선택한 정점에서 갈 수 있는 모든 Edge를 PQ에 넣기
			queue.addAll(adj[min.to]);
			visited[min.to] = true; // 선택했기 때문에 방문 표시
			cnt++;		// 선택한 정점 갯수 ++
		}
		System.out.println("min : " + result);
	}
}














