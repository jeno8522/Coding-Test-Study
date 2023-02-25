package com.ssafy.live04;

import java.util.Scanner;

public class Main_2023_G1_신기한소수_주창훈 {
	static int N;
	static StringBuilder sb;
	static int primeNum;
	static int[] headNum = {2,3,5,7};

	static void generatePrime(int cnt) {
		if (cnt == N) {
			if (isPrime(primeNum)) {
				sb.append(primeNum).append("\n");
				return;
			}
		}
		for (int i = 0; i <= 9; i++) {
			if (isPrime(primeNum)) {
				primeNum *= 10;
				primeNum += i;
				generatePrime(cnt + 1);
				primeNum /= 10;
			}
		}
	}

	static boolean isPrime(int num) {
		for (int i = 2; i * i <= num; i++) {
			if (num % i == 0)
				return false;
		}
		return true;
	}

	public static void main(String[] args) {
		sb = new StringBuilder();
		Scanner sc = new Scanner(System.in);

		N = sc.nextInt();
		
		
		for(int i = 0;i<4;i++) {
			primeNum = headNum[i];
			generatePrime(1);
		}



		System.out.println(sb);

	}

}
