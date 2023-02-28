package s0228;

import java.util.Arrays;

public class DisjointSetTreeRank {
	static int[] parents; // 원소의 부모를 저장하는 배열
	static int[] rank; // 랭크 표시를 위한 배열

	/**
	 * 서로소의 초기화 단계 - 아직 union 하기 전 단계이므로 자기 자신을 부모로 설정한다.
	 */
	public static void makeSet(int v) {
		parents[v] = v;
	}

	/**
	 * 원소의 대표 원소를 찾는 기능
	 * 
	 * @param v 원소
	 * @return 대표자
	 */
	public static int findSet(int v) {
		if (v == parents[v]) { // root를 찾은 경우
			return v;
		}

		return findSet(parents[v]);
	}

	public static void union(int u, int v) {
		int root1 = findSet(u);
		int root2 = findSet(v);

		// 같은 root이므로 합칠 필요가 없음
		if (root1 == root2)
			return;

		int rank1 = rank[root1];
		int rank2 = rank[root2];

		if (rank1 == rank2) { // rank가 같은 두 그룹은 어디에 붙여도 rank가 증가하는 것은 피할 수 없다.
			rank[root2]++; // 랭크 증가
			parents[root1] = root2;
			rank[root1] = 0;
		} else if (rank1 > rank2) { // root1의 rank가 크므로 root1 밑에 root2를 붙인다.
			// root1의 rank는 변화가 없으므로 증가 시키지 않는다.
			// root2는 더이상 root가 아니므로
			parents[root2] = root1; // 부모에 root1을 넣고
			rank[root2] = 0; // rank는 0으로 변화
		} else { // root2의 rank가 큰 상황
			parents[root1] = root2;
			rank[root1] = 0;
		}
	}

	public static void main(String[] args) {
		int N = 6;
		parents = new int[N + 1];
		rank = new int[N + 1];

		for (int i = 1; i <= N; i++) {
			makeSet(i);
		}

		union(4, 3);
		union(6, 5);
		union(5, 4);

		System.out.println((char) (findSet(6) + 'a' - 1));
		System.out.println((char) (findSet(4) + 'a' - 1));
		System.out.println(Arrays.toString(parents));
		System.out.println(Arrays.toString(rank));
	}

}
