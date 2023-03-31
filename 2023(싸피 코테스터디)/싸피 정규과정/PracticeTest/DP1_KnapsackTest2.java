package com.ssafy.dp;

import java.util.Scanner;

//배낭채우기 : 보석개수 1개 버전
/**
 * @author taeheekim
 */
public class DP1_KnapsackTest2 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int W = sc.nextInt();

		int[] weights = new int[N + 1];
		int[] profits = new int[N + 1];

		/* 뒤쪽 부터 채우기 때문에 w - weights[i]는 직전 item까지를 고려한 최대 가치가 저장되어 있다. */
		int[] D = new int[W + 1]; // 가치 테이블

		// i=0은 0으로 그대로 둠.
		for (int i = 1; i <= N; i++) {
			weights[i] = sc.nextInt();
			profits[i] = sc.nextInt();
		}
		int itemWeight = 0, itemBenefit = 0;
		// 모든 아이템에 대해서 반복
		for (int item = 1; item <= N; item++) {
			itemWeight = weights[item]; // 현 아이템의 무게
			itemBenefit = profits[item]; // 현 아이템의 가치

			// 현 아이템의 1부터 목표무게 까지의 가치테이블을 만든다.
			for (int weight = W; weight >= weights[item]; weight--) {
				if (D[weight] < itemBenefit + D[weight - weights[item]]) {
					D[weight] = itemBenefit + D[weight - weights[item]];
				}
			}
		}

		System.out.println(D[W]);
		sc.close();
	}

}
