package s0404;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main_17472_G1_다리만들기2_주창훈 {
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };
	static int N, M;
	static int[][] graph;
	static ArrayList<int[]>[] islandEdgePos;
//	static ArrayList<int[]> bridge;
	static HashSet<int[]> bridgeSet;
	static ArrayList<int[]> bridge;
	static ArrayDeque<int[]> queue;
	static boolean[][] visited;
	static int islandNum;
	static int[] parents;
	static int minValue;

	static boolean checkBoundary(int r, int c) {
		return 0 <= r && r < N && 0 <= c && c < M;
	}

	static void findIslandEdgePos() {
		visited = new boolean[N][M];
		islandEdgePos = new ArrayList[6];
		islandNum = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (graph[i][j] == 1 && !visited[i][j]) {
					islandEdgePos[islandNum] = new ArrayList<>();
					bfs(i, j, islandNum++);
				}
			}
		}
	}

	static boolean isIslandEdge(int r, int c) {
		for (int i = 0; i < 4; i++) {
			int nr = r + dr[i];
			int nc = c + dc[i];
			if (!checkBoundary(nr, nc))
				continue;
			if (graph[nr][nc] == 0)
				return true;
		}
		return false;
	}

	static void bfs(int i, int j, int num) {
		ArrayDeque<int[]> queue = new ArrayDeque<>();
		queue.addLast(new int[] { i, j });
		visited[i][j] = true;
		while (!queue.isEmpty()) {
			int[] now = queue.pollFirst();
			int r = now[0];
			int c = now[1];
			graph[r][c] = num + 1;
			if (isIslandEdge(r, c))
				islandEdgePos[num].add(new int[] { r, c });
			for (int k = 0; k < 4; k++) {
				int nr = r + dr[k];
				int nc = c + dc[k];
				if (!checkBoundary(nr, nc))
					continue;
				if (visited[nr][nc])
					continue;
				if (graph[nr][nc] == 1) {
					visited[nr][nc] = true;
					queue.addLast(new int[] { nr, nc });
				}

			}
		}
	}

	static void makeBridge() {
		bridgeSet = new HashSet<>();
		for (int i = 0; i < islandNum; i++) {
			for (int[] now : islandEdgePos[i]) {
				for (int j = 0; j < 4; j++) {
					dfs(now[0] + dr[j], now[1] + dc[j], i, 1, j);
				}

			}
		}
//		for (int[] is : bridgeSet) {
//			System.out.println(Arrays.toString(is));
//		}
//		System.out.println("----------------------------");
		bridge = new ArrayList<>(bridgeSet);
		bridge.sort((o1, o2) -> o1[2] - o2[2]);
	}

	static void dfs(int r, int c, int startIsland, int bridgeLength, int dir) {
		if (!checkBoundary(r, c)) {
			return;
		}
		if (graph[r][c] > 0 && graph[r][c] == startIsland) {
			return;
		}
		if (graph[r][c] > 0 && graph[r][c] != startIsland) {
			int endIsland = graph[r][c] - 1;

			if (bridgeLength >= 3) {
				bridgeSet.add(new int[] { startIsland, endIsland, bridgeLength - 1 });
			}
			return;
		}

		dfs(r + dr[dir], c + dc[dir], startIsland, bridgeLength + 1, dir);

	}

	static void makeSet() {
		parents = new int[islandNum];
		for (int i = 0; i < islandNum; i++) {
			parents[i] = i;
		}
	}

	static int findSet(int v) {
		if (parents[v] == v)
			return v;
		return parents[v] = findSet(parents[v]);
	}

	static boolean union(int a, int b) {
		int aRoot = findSet(a);
		int bRoot = findSet(b);

		if (aRoot == bRoot)
			return false;
		parents[bRoot] = aRoot;
		return true;
	}

	static boolean findMinValue() {
		makeSet();
		boolean isSuccess = false;
		int result = 0, cnt = 0;
		for (int[] now : bridge) {
			if(findSet(now[0])!=findSet(now[1])) {
				union(now[0],now[1]);
				result += now[2];
				cnt++;
			}
		}
		if(cnt + 1 == islandNum) {
			isSuccess = true;
		}
		minValue = result;
		return isSuccess;
	}

	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		graph = new int[N][M];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		findIslandEdgePos();
		makeBridge();
		boolean isSuccess;
		isSuccess = findMinValue();
		if(isSuccess) {
			System.out.println(minValue);
		}
		else {
			System.out.println(-1);
		}
//		for (int[] elem : bridge) {
//			System.out.println(Arrays.toString(elem));
//		}
//		for (int[] e : graph) {
//			System.out.println(Arrays.toString(e));
//		}

//		int cnt = 0;
//		System.out.println(islandNum);
//		for (ArrayList<int[]> elem : islandEdgePos) {
//			System.out.print("섬 번호 : " + cnt++);
//			for (int[] e : elem) {
//				System.out.print(Arrays.toString(e) + " ");
//			}
//			System.out.println();
//		}
	}

}
