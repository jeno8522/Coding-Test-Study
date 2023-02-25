package com.ssafy.temporary;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class PermutationCombinationSubsetTest {
	static int[] numbers;
	static boolean[] isSelected;
	static int N;
	static int M;
	static int mode;
	static int S;
	static StringBuilder sb;

	static void permutation1(int cnt) { // 순열
		if (cnt == M) {
			for (int num : numbers) {
				sb.append(num).append(" ");
			}
			sb.append("\n");
			return;
		}
		for (int i = 1; i <= N; i++) {
			if (isSelected[i])
				continue;
			numbers[cnt] = i;
			isSelected[i] = true;
			permutation1(cnt + 1);
			isSelected[i] = false;
		}

	}

	static void permutation2(int cnt) {
		if (cnt == M) {
			for (int num : numbers) {
				sb.append(num).append(" ");
			}
			sb.append("\n");
			return;
		}
		for (int i = 1; i <= N; i++) {
			numbers[cnt] = i;
			permutation2(cnt + 1);

		}

	}

	static void combination1(int cnt, int start) {
		if (cnt == M) {
			for (int num : numbers) {
				sb.append(num).append(" ");
			}
			sb.append("\n");
			return;
		}
		for (int i = start; i <= N; i++) {
			numbers[cnt] = i;
			combination1(cnt + 1, i + 1);
		}
	}

	static void combination2(int cnt, int start) {
		if (cnt == M) {
			for (int num : numbers) {
				sb.append(num).append(" ");
			}
			sb.append("\n");
			return;
		}
		for (int i = start; i <= N; i++) {
			numbers[cnt] = i;
			combination2(cnt + 1, i);
		}
	}

	static void subSet(int cnt) {
		if (cnt == N) {
			for (int i = 0; i < N; i++) {
				System.out.print(isSelected[i] ? numbers[i] : "X");
				System.out.print(" ");
			}
			System.out.println();
			return;
		} else {
			isSelected[cnt] = true;
			subSet(cnt + 1);
			isSelected[cnt] = false;
			subSet(cnt + 1);
		}
	}

	static void subSetSum(int cnt, int sum) {
		if (cnt == N) {
			if (sum == S) {
				for (int i = 0; i < N; i++) {
					System.out.print(isSelected[i] ? numbers[i] : "X");
					System.out.print(" ");
				}
				System.out.println();
//					return;
			}
			return;

		} else {
			isSelected[cnt] = true;
			subSetSum(cnt + 1, sum + numbers[cnt]);
			isSelected[cnt] = false;
			subSetSum(cnt + 1, sum);
		}
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		String str = br.readLine();
		st = new StringTokenizer(str);
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		mode = Integer.parseInt(st.nextToken());
		numbers = new int[M];
		sb = new StringBuilder();
		switch (mode) {
		case 1:
			isSelected = new boolean[N + 1];
			permutation1(0);
			System.out.println(sb.toString());
			break;
		case 2:
			permutation2(0);
			System.out.println(sb.toString());
			break;
		case 3:
			combination1(0, 1);
			System.out.println(sb.toString());
			break;
		case 4:
			combination2(0, 1);
			System.out.println(sb.toString());
			break;
		case 5:
			numbers = new int[N + 1];
			str = br.readLine();
			st = new StringTokenizer(str);
			for (int i = 0; i < N; i++) {
				numbers[i] = Integer.parseInt(st.nextToken());
			}
			isSelected = new boolean[N + 1];
			subSet(0);
			break;
		case 6:
			numbers = new int[N + 1];
			str = br.readLine();
			st = new StringTokenizer(str);
			for (int i = 0; i < N; i++) {
				numbers[i] = Integer.parseInt(st.nextToken());
			}
			isSelected = new boolean[N + 1];
			S = Integer.parseInt(br.readLine());
			subSetSum(0, 0);
			break;
		default:
			break;
		}
	}

}
