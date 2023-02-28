package s0228;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

/**
 * 시간 복잡도 O(V^3)
 * 
 */

public class MST_PRIM {

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// 데이터 입력 받기
		int N = Integer.parseInt(br.readLine());
		int[][] map = new int[N][N]; // 노드의 인접 및 가중치 정보
		boolean[] visited = new boolean[N]; // 노드의 방문 처리

		StringTokenizer st = null;
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < N; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		// 선택된 정점을 저장하는 list
		ArrayList<Integer> selected = new ArrayList<>(N);
		int index;
		int min; // 갈 수 있는 Edge 중에서 최솟값
		int result = 0; // MST 값

		// 임의의 정점 하나 선택
		selected.add(0); // 인접 행렬로 되어 있어서 0번 부터 찾기
		visited[0] = true;

		// 모든 정점을 반복 하면서
		for (int i = 0; i < N - 1; i++) {	// 임의의 정점을 초기에 하나 선택하고 반복문을 돌기 때문에
			min = Integer.MAX_VALUE;
			index = 0;

			// 갈 수 있는 모든 Edge들을 반복하면서 최소 비용의 Edge를 선택
			// 1. 선택한 정점을 반복하면
			for (Integer v : selected) {
				// 2. 인접된 노드 중에 안 가본 노드 중 최소 비용을 찾기
				for (int j = 0; j < N; j++) {
					if (map[v][j] != 0 && !visited[j] && map[v][j] < min) {
						min = map[v][j];
						index = j;
					}
				}
			}
			// 최소 비용의 노드를 찾았다면 해당 노드 방문 표시 하고, 선택한 노드 처리, 최솟값 갱신
			result += min; // 선택된 최소 비용을 누적해 주기
			selected.add(index); // 최솟값으로 선택된 정점
			visited[index] = true; // 선택했기 때문에 방문 표시
		}
		System.out.println("min : " + result);
		System.out.println(selected);
	}
}
