
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main_17135_G3_캐슬디펜스_주창훈 {
	static int N, M, D;
	static int[][] graph;
	static int[][] saveGraph;
	static int ans;

	public static void main(String[] args) throws NumberFormatException, IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		D = Integer.parseInt(st.nextToken());

		graph = new int[N + 1][M + 1];
		saveGraph = new int[N + 1][M + 1];
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= M; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
				saveGraph[i][j] = graph[i][j];
			}
		}
		start();

		System.out.println(ans);
	}
	
	public static void start() {
		ArrayList<Integer> archer = new ArrayList<>();
		ans = 0;
		combination(1, 0, archer);
	}

	public static void copy() {	//턴이 지나고 변동된 그래프를 원상복귀
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= M; j++) {
				graph[i][j] = saveGraph[i][j];
			}
		}
	}

	public static int distance(int r1, int r2, int c1, int c2) {
		return Math.abs(r1 - r2) + Math.abs(c1 - c2);
	}

	public static void combination(int start, int cnt, ArrayList<Integer> archer) {
		if (cnt == 3) {
			copy();
			attack(archer);
			return;
		}

		for (int i = start; i <= M; i++) {
			archer.add(i);
			combination(i + 1, cnt + 1, archer);
			archer.remove(archer.size() - 1);
		}
	}

	public static void attack(ArrayList<Integer> archer) {
		int res = 0;

		for (int n = 1; n <= N; n++) {
			boolean[][] visited = new boolean[N + 1][M + 1];
			for (int k = 0; k < archer.size(); k++) {
				int now_archerPos = archer.get(k);	//현재 궁수 위치
				int killD = Integer.MAX_VALUE;		//죽인 적의 정보
				int killR = Integer.MAX_VALUE;
				int killC = Integer.MAX_VALUE;

				for (int i = 1; i <= N; i++) {
					for (int j = 1; j <= M; j++) {
						if (graph[i][j] == 1) {		//적이면
							if (killD >= distance(i, N + 1, j, now_archerPos)) {	//지금 죽인 적과의 거리가 저장된 적과의 거리보다 작거나 같다면
								if (killD > distance(i, N + 1, j, now_archerPos)) { // 작다면 거리, 좌표 갱신
									killD = distance(i, N + 1, j, now_archerPos);
									killR = i;
									killC = j;
								} else {	//같다면
									if (killC > j) {	//같은데 더 왼쪽에 있다면 좌표만 갱신
										killR = i;
										killC = j;
									}
								}
							}
						}
					}
				}

				if (killD <= D) {	//죽인 적까지의 거리가 궁수의 사정거리 안이면 방문 처리
					visited[killR][killC] = true;
				}
			}

			for (int i = 1; i <= N; i++) {
				for (int j = 1; j <= M; j++) {
					if (visited[i][j]) {	// 방문 처리되어있으면 count 해줌
						graph[i][j] = 0;	// 해당 적을 없앰
						res++;
					}
				}
			}


			for (int i = N; i >= 1; i--) {		//graph를 한칸씩 아래로
				for (int j = 1; j <= M; j++) {
					graph[i][j] = graph[i - 1][j];
				}
			}
		}

		ans = Math.max(ans, res);
	}

}
