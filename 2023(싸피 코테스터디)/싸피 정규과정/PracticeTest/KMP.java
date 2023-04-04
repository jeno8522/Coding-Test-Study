package s0404;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class KMP {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		char[] text = br.readLine().toCharArray();
		char[] pattern = br.readLine().toCharArray();

		int tLen = text.length;
		int pLen = pattern.length;
		if(tLen < pLen) {
			System.out.println(0);
			System.exit(1);
		}
		// Fail 함수 만들기 (부분 일치 문자열의 개수가 몇 개인지 count)
		int[] fail = new int[pLen];
		/*
		 * i : 접미사 포인터 ( i = 1 부터 시작 ) j : 접두사 포인터
		 */
		for (int i = 1, j = 0; i < pLen; i++) {
			while (j > 0 && pattern[i] != pattern[j]) {
				j = fail[j - 1];
			}
			if (pattern[i] == pattern[j])
				fail[i] = ++j;
		}
//		System.out.println(Arrays.toString(fail));

		Deque<Integer> list = new ArrayDeque<Integer>();

		for (int i = 0, j = 0; i < tLen; i++) {
			// 본문과 패턴이 맞지 않으면 j 위치를 이동
			while (j > 0 && text[i] != pattern[j])
				j = fail[j - 1];
			// 두 글자가 일치하면
			if (text[i] == pattern[j]) {
				if (j == pLen - 1) { // j가 패턴의 끝이므로, 본문과 패턴이 일치
					list.add((i + 1) - pLen + 1); // 패턴이 일치한 시작 위치
					j = fail[j];
				} else {
					j++;
				}
			}
		}
		int cnt = list.size();
		System.out.println(cnt);
		if (cnt > 0) {
			for (int elem : list) {
				System.out.println(elem);
			}
		}
//		System.out.println();
	}

}
