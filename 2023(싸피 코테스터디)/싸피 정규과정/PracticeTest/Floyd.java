package lecture.dp;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Floyd {
//	static final int INF = Integer.MAX_VALUE >> 2;
	static final int INF = 999999;
	static int N, map[][];

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		map = new int[N][N];
		StringTokenizer st = null;

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				// 연결 되지 않은 경로이므로 INF로 초기화
				if (i != j && map[i][j] == 0) {
					map[i][j] = INF;
				}
			}
		}
		for (int k = 0; k < N; k++) { // 경유지
			for (int i = 0; i < N; i++) { // 출발지
//				if (k == i)		이 코드로 연산 갯수가 늘어나므로 오히려 더 느려짐
//					continue; // 출발지와 경유지가 같다면 다음 경유지로 continue
				for (int j = 0; j < N; j++) { // 도착지
//					if (i == j || k == j) // 출발지와 도착지가 같거나, 경유지와 도착지가 같다면 다음 경유지로 continue
//						continue;	이 코드로 연산 갯수가 늘어나므로 오히려 더 느려짐
					// 직접 가는 비용 경유지를 거쳐서 가는 비용 보다 크다면
					if (map[i][j] > map[i][k] + map[k][j])
						map[i][j] = map[i][k] + map[k][j]; // 최소 비용으로 dp값 갱신
				}
			}
		}
		for (int[] line : map) {
			System.out.println(Arrays.toString(line));
		}
	}

}
