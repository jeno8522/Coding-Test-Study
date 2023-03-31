package pcsPractice.real;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;

/**
*
[입력데이타]
6 11
0 1 4
0 2 2 
0 5 25
1 3 8
1 4 7
2 1 1
2 4 4
3 5 6
4 0 3
4 3 5
4 5 12
*
*/
public class Dijkstra_PQ2 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int V = sc.nextInt();
		int E = sc.nextInt();
		ArrayList<int[]>[] adj = new ArrayList[V];
		for (int i = 0; i < V; i++)
			adj[i] = new ArrayList<>();
		for (int i = 0; i < E; i++) {
			adj[sc.nextInt()].add(new int[] { sc.nextInt(), sc.nextInt() });
		}
		PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]);
		int[] D = new int[V];
		for (int i = 0; i < V; i++) {
			if (i == 0) {
				D[i] = 0;
				pq.add(new int[] { i, D[i] });
			} else {
				D[i] = Integer.MAX_VALUE;
			}
		}
		while (!pq.isEmpty()) {
			int[] now = pq.poll();
			if (now[1] > D[now[0]])
				continue;
			for (int[] next : adj[now[0]]) {
				if (D[next[0]] > now[1] + next[1]) {
					D[next[0]] = now[1] + next[1];
					pq.add(new int[] { next[0], D[next[0]] });
				}
			}
		}
		System.out.println(Arrays.toString(D));
	}
}
