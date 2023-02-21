import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main_2563_S5_색종이_주창훈 {
	static int N;
	static int res = 0;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		boolean[][] check = new boolean[101][101];
		for (int t = 0; t < N; t++) {
			st = new StringTokenizer(br.readLine());
			int r = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			for (int i = r; i < r + 10; i++) {
				for (int j = c; j < c + 10; j++) {
					if (check[i][j] == true) {
						continue;
					}
					check[i][j] = true;
					res++;
				}
			}
		}
		System.out.println(res);
	}

}