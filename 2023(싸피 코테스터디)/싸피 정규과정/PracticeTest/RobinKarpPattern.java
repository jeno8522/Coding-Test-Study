package s0404;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class RobinKarpPattern {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		char[] text = br.readLine().toCharArray();
		char[] pattern = br.readLine().toCharArray();

		long pHash = 0, tHash = 0, power = 1;
		long base = 26;	//대소문자 구별하려면 52
		long mod = 1000000009;
		int tLen = text.length;
		int pLen = pattern.length;
		Deque<Integer> list = new ArrayDeque<>();

		// pattern의 개수만큼 본문의 hash 와 pattern의 hash를 구하기 <= k개를 미리 구하기
		if(tLen < pLen) {
			System.out.println(0);
			System.exit(1);
		}
		for (int i = 0; i < pLen; i++) {
			pHash = (pHash * base) % mod;
			pHash = (pHash + pattern[i]) % mod;
			tHash = (tHash * base) % mod;
			tHash = (tHash + text[i]) % mod;

			if (i < pLen - 1)
				power = (power * base) % mod;
		}
		if (pHash == tHash) {
			list.add(1);
		}
		for (int i = 1; i <= tLen - pLen; i++) {
			// 본문의 새로운 hash 만들기
			// 윈도우의 맨 앞 부분을 빼주고
			tHash = (((tHash - (text[i - 1] * power) % mod + mod) % mod * base) + text[i + pLen - 1]) % mod; // 윈도우의 맨 뒷 부분에 추가
																												
			if (pHash == tHash)
				list.add(i + 1);
			// 만약 hash 충돌이 된 경우 문자열을 하나씩 비교한다.
		}

		System.out.println(list.size());
		for (int index : list) {
			System.out.println(index);
		}

	}

}