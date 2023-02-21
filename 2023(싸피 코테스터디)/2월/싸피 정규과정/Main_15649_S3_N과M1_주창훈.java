package algorithm;

import java.util.Scanner;

public class Main {
 
	public static int[] result;
	public static int[] visit;
 
	public static void main(String[] args) {
 
		Scanner in = new Scanner(System.in);
 
		int N = in.nextInt();
		int M = in.nextInt();
 
		result = new int[M];
		visit = new int[N];		// 해당 숫자 사용 여부
		permutation(N, M, 0);
 
	}
 
	public static void permutation(int N, int M, int depth) {
		if (depth == M) {
			for (int val : result) {
				System.out.print(val + " ");
			}
			System.out.println();
			return;
		}
		
		for(int i = 0; i < N; i++) {
			if(visit[i] == 0) {
				visit[i] = 1;
				result[depth] = i + 1;
				permutation(N, M, depth + 1);
				visit[i] = 0;
			}
		}

	}
 
}