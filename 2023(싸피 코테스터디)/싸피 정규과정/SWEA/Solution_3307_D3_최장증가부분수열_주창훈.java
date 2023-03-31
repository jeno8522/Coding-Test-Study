package com.ssafy.dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution_3307_D3_최장증가부분수열_주창훈 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			int N = Integer.parseInt(br.readLine());
			int[] arr = new int[N];
			int[] C = new int[N];
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				arr[i] = Integer.parseInt(st.nextToken());
			}
			int k = 0;
			C[k++] = arr[0];
			for (int i = 1; i < N; i++) {
				int temp = Arrays.binarySearch(C, 0, k, arr[i]);
				temp = Math.abs(temp) - 1;
				C[temp] = arr[i];
				if (k == temp) {
					k++;
				}
			}
			System.out.println("#" + tc + " " + k);
		}

	}

}
