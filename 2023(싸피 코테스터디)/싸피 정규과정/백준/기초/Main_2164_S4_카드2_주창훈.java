package com.ssafy.subset;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class Main_2164_S4_카드2_주창훈 {
	static int N;
	static Deque<Integer> card;
	static int res;

	static void pickCard() {
		while (true) {
			if(card.size() == 1) {
				res = card.pollFirst();
				return;
			}
			card.pollFirst();

			res = card.pollFirst();

			card.addLast(res);
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		card = new ArrayDeque<>();
		for (int num = 1; num <= N; num++) {
			card.addLast(num);
		}
		pickCard();
		System.out.println(res);
	}

}
