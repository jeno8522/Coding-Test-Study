package s0228;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_G4_17471_게리멘더링_주창훈 {
	static int N;
	static int[] weights;
	static ArrayList<Integer>[] city;
	static ArrayList<Integer> combi;
	static int minValue = Integer.MAX_VALUE;
	static int totalValue = 0;
	static boolean candivide = false;

	static boolean isConnected(ArrayList<Integer> AorB ,boolean[] visited, boolean check) {
		visited[AorB.get(0)] = !check;
		ArrayDeque<Integer> queue = new ArrayDeque<>();
		queue.addLast(AorB.get(0));
		while (!queue.isEmpty()) {
			int now = queue.pollFirst();
			for (Integer next : city[now]) {
				if (visited[next] == !check)
					continue;
				visited[next] = !check;
				queue.addLast(next);
			}
		}
		for (int i = 1; i <= N; i++) {
			if (visited[i] == check) // visited에 check가 있으면
				return false;
		}
		return true;
	}
	
	

	static void combination(int cnt, int start, int limit) {
//		System.out.println(combi.toString());
		if (cnt == limit) {
//			System.out.println(cnt);
			boolean isValid = false;
			boolean[] visited = new boolean[N + 1];
			for (Integer num : combi) {
				visited[num] = true;
			}
			if (isConnected(combi,visited, true))
				isValid = true;

			if (isValid) {
				visited = new boolean[N + 1];
				for (Integer num : combi) {
					visited[num] = true;
				}
				ArrayList<Integer> notCombi = new ArrayList<>();
				for (int i = 1; i <= N; i++) {
					if(!combi.contains(i)) {
						notCombi.add(i);
					}
				}
//				System.out.println(notCombi.toString());
				if(isConnected(notCombi, visited, false)) {
					calMin();
					candivide = true;
				}
				
			}

			return;
		}
		for (int i = start; i <= N; i++) {
			combi.add(i);
			combination(cnt + 1, i + 1, limit);
			combi.remove(combi.size() - 1);
		}

	}

	static void calMin() {
		int ASum = 0;
		for (Integer num : combi) {
			ASum += weights[num];
		}
		int BSum = totalValue - ASum;

		minValue = Math.min(minValue, Math.abs(ASum - BSum));
	}

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		weights = new int[N + 1];
		st = new StringTokenizer(br.readLine());
		city = new ArrayList[N + 1];
		for (int i = 1; i <= N; i++) {
			weights[i] = Integer.parseInt(st.nextToken());
			city[i] = new ArrayList<>();
		}
		totalValue = Arrays.stream(weights).sum();
//		System.out.println(totalValue);

		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			int adj = Integer.parseInt(st.nextToken());
			for (int j = 0; j < adj; j++) {
				city[i].add(Integer.parseInt(st.nextToken()));
			}
		}
		combi = new ArrayList<>();
		for (int i = 1; i <= N / 2; i++) {
			combination(0, 1, i);
		}
		if(candivide)
			System.out.println(minValue);
		else
			System.out.println(-1);
	}

}
