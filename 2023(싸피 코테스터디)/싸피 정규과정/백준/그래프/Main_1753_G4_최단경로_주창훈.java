

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;


class Node implements Comparable<Node>{
	int vertex, weight;
	
	public Node(int vertex, int weight) {
		super();
		this.vertex = vertex;
		this.weight = weight;
	}

	@Override
	public int compareTo(Node o) {
		return this.weight - o.weight;
	}
}

public class Main_G4_1753_최단경로_주창훈 {
	static int V;
	static int E;
	static ArrayList<Node>[] graph;
	static int [] distance;
	
	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		V = Integer.parseInt(st.nextToken());
		E = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		int start = Integer.parseInt(st.nextToken());
		graph = new ArrayList[V+1];
		for (int i = 1; i <= V; i++) {
			graph[i] = new ArrayList<>();
		}
		for (int i = 0; i < E; i++) {
			st = new StringTokenizer(br.readLine());
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			int weight = Integer.parseInt(st.nextToken());
			graph[from].add(new Node(to, weight));
		}
		distance = new int[V+1];
		Arrays.fill(distance, Integer.MAX_VALUE);
		
		distance[start] = 0;
		dijkstra(start);
		
		for (int i = 1; i < distance.length; i++) {
			if(distance[i] == Integer.MAX_VALUE)
				System.out.println("INF");
			else
				System.out.println(distance[i]);
		}
	}

	private static void dijkstra(int start) {
		PriorityQueue<Node> pq = new PriorityQueue<>();
		pq.add(new Node(start, 0));
		
		while(!pq.isEmpty()) {
			Node now = pq.poll();
			for (Node next : graph[now.vertex]) {
				if(distance[next.vertex] > now.weight + next.weight) {
					distance[next.vertex] = now.weight + next.weight;
					pq.add(new Node(next.vertex, distance[next.vertex]));
				}
			}
		}
	}

}








