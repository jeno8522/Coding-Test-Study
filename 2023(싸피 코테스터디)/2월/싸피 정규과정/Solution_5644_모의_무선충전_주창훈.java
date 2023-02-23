import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Solution_5644_모의_무선충전_주창훈 {
	static int A, M;
	static int[][] graph;
	static int[] user1;
	static int[] user2;
	static int maxCharge = 0;
	static int[] dr = { 0, -1, 0, 1, 0 };
	static int[] dc = { 0, 0, 1, 0, -1 };

	public static int move(int user1R, int user1C, int user2R, int user2C) {
		int charge = 0;
		int tmpCharge = 0;
		for (int i = 0; i < A; i++) {
			for (int j = 0; j < A; j++) {
				int user1P = check(i, user1R, user1C);
				int user2P = check(j, user2R, user2C);
				if(i == j) {
					charge = Math.max(user1P, user2P);
				}
				else {
					charge = user1P + user2P;
				}
				tmpCharge = Math.max(tmpCharge, charge);
			}
		}
		return tmpCharge;
		
	}
	public static int check(int bcNum, int userR, int userC) {
			return graph[bcNum][2] >= Math.abs(graph[bcNum][0] - userR) + Math.abs(graph[bcNum][1] - userC) ? graph[bcNum][3] : 0;
	}

	public static void main(String[] args) throws IOException {
		//System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int T = Integer.parseInt(st.nextToken());
		for (int test_case = 1; test_case <= T; test_case++) {
			st = new StringTokenizer(br.readLine());
			M = Integer.parseInt(st.nextToken());
			A = Integer.parseInt(st.nextToken());
			user1 = new int[M];
			user2 = new int[M];
			graph = new int[A][4];
			maxCharge = 0;
			int user1R = 1, user1C = 1;
			int user2R = 10, user2C = 10;
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < M; i++) {
				user1[i] = Integer.parseInt(st.nextToken());
			}
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < M; i++) {
				user2[i] = Integer.parseInt(st.nextToken());
			}
			
			for (int i = 0; i < A; i++) {
				st = new StringTokenizer(br.readLine());
				graph[i][1] = Integer.parseInt(st.nextToken()); // row
				graph[i][0] = Integer.parseInt(st.nextToken()); // column
				graph[i][2] = Integer.parseInt(st.nextToken()); // distance
				graph[i][3] = Integer.parseInt(st.nextToken()); // power
			}
			maxCharge += move(user1R, user1C, user2R, user2C);
			for (int i = 0; i < M; i++) {
				
				user1R += dr[user1[i]];
				user1C += dc[user1[i]];
				user2R += dr[user2[i]];
				user2C += dc[user2[i]];
				maxCharge += move(user1R, user1C, user2R, user2C);
 			}
			System.out.print("#" + test_case + " " + maxCharge);
			System.out.println();
			
		}
	}

}
