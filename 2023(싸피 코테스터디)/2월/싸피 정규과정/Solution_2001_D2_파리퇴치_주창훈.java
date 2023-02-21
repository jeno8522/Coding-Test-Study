import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_2001_D2_파리퇴치_주창훈 {
	static BufferedReader br;
	static StringTokenizer st;
	static int n;
	static int m;
	static int [][] graph;
	static int killMax;
	
	static void killFlies() {
		int killCnt = 0;
		
		for (int i = 0; i < n - m + 1; i++) {
			for (int j = 0; j < n - m + 1; j++) {
				killCnt = 0;
				for (int k = 0; k < m; k++) {
					for (int l = 0; l < m; l++) {
						killCnt += graph[i + k][j + l];
					}
				}
				if(killMax < killCnt) killMax = killCnt;
			}
		}
	}
	public static void main(String args[]) throws Exception {

		//System.setIn(new FileInputStream("res/input.txt"));
		br = new BufferedReader(new InputStreamReader(System.in));
		int T;
		T = Integer.parseInt(br.readLine());

		for (int test_case = 1; test_case <= T; test_case++) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			graph = new int[n][n];
			for (int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < n; j++) {
					graph[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			killMax = Integer.MIN_VALUE;
			killFlies();
			System.out.println("#"+test_case + " " + killMax);
		}
	}
}