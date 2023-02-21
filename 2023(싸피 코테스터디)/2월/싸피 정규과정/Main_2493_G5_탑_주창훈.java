
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;


public class Main_2493_G5_탑_주창훈 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		Stack<Integer> save = new Stack<Integer>();
		Stack<Integer> index = new Stack<Integer>(); // 위치 저장

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());

		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 1; i <= N; i++) {
			int now = Integer.parseInt(st.nextToken());
			while (true) {
				if (!save.empty()) {			// 스택이 비어있지 않다면
					int top = save.peek();
					if (top > now) {							// top이 now보다 크다면 
						System.out.print(index.peek() + " ");	// top의 index 출력
						save.push(now);	//now value, index 를 save에 저장
						index.push(i);
						break;
					} else { // top이 now 보다 작으면 pop
						save.pop();
						index.pop();

					}
				} else { 	// 처음 탑 저장 or save에 저장된 값들 보다 더 큰 값
					System.out.print("0 ");	// 수신 받을 곳 없음
					save.push(now);
					index.push(i);
					break;

				}

			}

		}
	}

}