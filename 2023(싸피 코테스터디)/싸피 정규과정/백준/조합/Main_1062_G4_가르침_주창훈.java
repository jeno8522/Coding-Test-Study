package s0224;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.StringTokenizer;

public class Main_1062_G4_가르침_주창훈 {
	static int N, K;
	static boolean[] visited = new boolean[26];
	static HashSet<Integer> set;
	static ArrayList<Integer>[] sentence;
	static int[] comb;
	static ArrayList<Integer> numbers = new ArrayList<>();
	static int answer = 0;

	static void start() {	
		for (int i = K; i >= 0; i--) {	// K개부터 0개까지 몇개의 단어를 배울 수 있는 지 체크
			combination(0, 0, i);
		}
	}

	static void combination(int cnt, int start, int limit) {	//설정한 limit개의 조합으로 check 함수를 호출
		if (cnt == limit) {
			check(comb);
			return;
		}
		for (int i = start; i < numbers.size(); i++) {
			comb[cnt] = numbers.get(i);
			combination(cnt + 1, i + 1, limit);
		}
	}

	static void check(int[] word) {	// 배울 수 있는 단어의 조합으로 몇개의 단어를 배울 수 있는 지 체크하는 함수
		int cnt = 0;
		boolean isValid = false;
		for (int i = 0; i < sentence.length; i++) {
			
			if (sentence[i].isEmpty()) {	// 단어의 길이가 0이다 == base문자로도 이미 배울 수 있는 단어
				cnt++;
			}
			else {
				for (int j = 0; j < sentence[i].size(); j++) {
					int tmp = sentence[i].get(j);
					isValid = false;
					for (int num : word) {
						if (num == tmp) {
							isValid = true; // 조합으로 뽑은 문자중에서 해당 문자를 찾음
							break;
						}
					}
					if (!isValid)
						break; // 해당 문자가 없으면 break
				}
				if (isValid)	// 단어의 모든 문자를 통과하면 count + 1
					cnt++;
			}
		}
		answer = Math.max(answer, cnt);	// 배울 수 있는 언어 개수의 최댓값

	}
	static boolean baseCheck(int num) {
		return num != 'a' - 'a' && num != 'c' - 'a' && num != 't' - 'a' && num != 'i' - 'a' && num != 'n' - 'a';
	}
	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("res/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		K -= 5;
		
		if(K < 0) {	//base를 알기위한 최소 단어수보다 작다면 0 출력, 종료
			System.out.println(0);
			System.exit(0);
		}
		visited['a' - 'a'] = true;	//base로 알고 있는 문자 visited 체크
		visited['c' - 'a'] = true;
		visited['t' - 'a'] = true;
		visited['i' - 'a'] = true;
		visited['n' - 'a'] = true;
		sentence = new ArrayList[N];
		for (int i = 0; i < N; i++) {
			String str = br.readLine();
			str = str.substring(4, str.length() - 4);	//주어진 단어 처음과 끝 base 부분 자름
			sentence[i] = new ArrayList<>();
			set = new HashSet<>();
			for (int j = 0; j < str.length(); j++) {	//주어진 단어 중복제거
				set.add(str.charAt(j) - 'a');
			}
			Iterator<Integer> it = set.iterator();
			while (it.hasNext()) {
				int tmp = it.next();
				visited[tmp] = true;	// 주어진 단어의 문자들을 visited 체크 
				if (baseCheck(tmp)) {	// base 부분 아닌부분만 단어로 취급
					sentence[i].add(tmp);
				}
				
			}
		}
		comb = new int[K];
		for (int i = 0; i < 26; i++) {
			if (visited[i] && baseCheck(i)) {	//단어에 쓰인 부분과 base가 아닌 문자만 조합으로 뽑을 전체 집합으로 사용
				numbers.add(i);
			}
		}
		start();
		System.out.println(answer);

	}

}
