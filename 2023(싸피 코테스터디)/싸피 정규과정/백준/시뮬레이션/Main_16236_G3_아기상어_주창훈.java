package s0302;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.StringTokenizer;

class fish{
	int r, c, t;

	public fish(int r, int c, int t) {
		super();
		this.r = r;
		this.c = c;
		this.t = t;
	}

	@Override
	public String toString() {
		StringBuilder builder = new StringBuilder();
		builder.append("fish [r=").append(r).append(", c=").append(c).append(", t=").append(t).append("]");
		return builder.toString();
	}
	
}
public class Main_16236_G3_아기상어_주창훈 {
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };
	static int N;
	static int[][] graph;
	static boolean[][] visited;
	static int size = 2;
	static int result = 0;
	static int startR, startC;
	
	static fish bfs(int r, int c) {
		visited[r][c] = true;
		ArrayDeque<int[]> queue = new ArrayDeque<>();
		fish food = new fish(Integer.MAX_VALUE,Integer.MAX_VALUE,Integer.MAX_VALUE);
		queue.addLast(new int[] {r,c,0});
		
		while(!queue.isEmpty()) {
			int[] now = queue.pollFirst();
			for (int i = 0; i < 4; i++) {
				int nr = now[0] + dr[i];
				int nc = now[1] + dc[i];
				int time = now[2];
				if(nr <0 || nr >=N || nc <0 || nc >=N) continue;
				if(graph[nr][nc] > size || visited[nr][nc]) continue;
				else if(graph[nr][nc]==0 || size == graph[nr][nc]) {
					queue.addLast(new int[] {nr,nc,time+1});
					visited[nr][nc] = true;
				}
				else if(graph[nr][nc] < size) {
					queue.addLast(new int[] {nr,nc,time+1});
					visited[nr][nc] = true;
					if(food.t > time + 1) food = new fish(nr,nc,time+1);
					else if(food.t == time + 1) {
						if(food.r > nr) food = new fish(nr,nc,time+1);
						else if(food.r == nr) {
							if(food.c > nc) food = new fish(nr,nc,time+1);
						}
					}
				}
				
			}
		}
		return food;
	}

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		graph = new int[N][N];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
				if(graph[i][j] == 9) {
					startR = i;
					startC = j;
				}
			}
		}
		
		
		int foodCnt = 0;
		while(true) {
			visited = new boolean[N][N];
			graph[startR][startC] = 0;
			fish food = bfs(startR, startC);
//			System.out.println(food.toString());
			if(food.t == Integer.MAX_VALUE) break;
			foodCnt++;
			if(foodCnt == size) {
				size++;
				foodCnt = 0;
			}
			result += food.t;
			startR = food.r;
			startC = food.c;
		}
		System.out.println(result);
		
	}

}
