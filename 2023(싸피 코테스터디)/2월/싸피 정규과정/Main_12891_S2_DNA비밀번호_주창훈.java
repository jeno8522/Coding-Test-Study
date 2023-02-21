package com.ssafy.subset;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main_12891_S2_DNA비밀번호_주창훈 {

	static int S;
	static int P;
	static int answer;
	static String DNA;
	static HashMap<Character, int[]> hm = new HashMap<Character, int[]>();
	static char[] dna = { 'A', 'C', 'G', 'T' };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		S = Integer.parseInt(st.nextToken());  // 제공되는 문자열 길이
		P = Integer.parseInt(st.nextToken());  //비밀번호 문자열 길이
		DNA = br.readLine();         // 제공되는 문자열
		st = new StringTokenizer(br.readLine());  // { A, C, G , T} 가 최조 들어가야 하는 문자열 최소 개수

		// HashMap의 구조 : (DNA문자, {현재 카운트, 최소 조건})
		for (char c : dna) {   //{ 'A', 'C', 'G', 'T' };
			hm.put(c, new int[] { 0, Integer.parseInt(st.nextToken()) });
		}

		// 처음 P만큼 자른 문자열을 카운트하고 조건을 만족하는지 체크
		for (int i = 0; i < P; i++) {
			hm.get(DNA.charAt(i))[0]++;    // 제공되는 문자열을 짤라서 (ACGT만)같은 문자 카운팅
		}
		if (isFull())
			answer++;

		// 인덱스를 1씩 증가시켜가며 가장 왼쪽 문자 삭제, 가장 오른쪽 문자 추가
		// 카운트를 모두 새로 하는것이 아닌 왼쪽 끝은 -1 오른쪽 끝은 +1한다.
		for (int i = 0; i < S - P; i++) {
			hm.get(DNA.charAt(i))[0] -= 1;  // 왼쪽 문자 1개 제거하면서 카운팅 된거 빼기
			hm.get(DNA.charAt(i + P))[0] += 1;  //오른쪽 문자 하나 추가하면서 카운팅
			if (isFull())
				answer++;
		}
		System.out.println(answer);

	}
	
   // 최소 문자 개수 조건을 만족할 문자들이 있는지
	public static boolean isFull() {
		for (char c : dna) {
			if (hm.get(c)[0] < hm.get(c)[1])
				return false;
		}
		return true;

	}

}
