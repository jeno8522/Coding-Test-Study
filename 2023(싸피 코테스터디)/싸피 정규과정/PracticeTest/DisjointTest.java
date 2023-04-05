import java.lang.reflect.Array;
import java.util.Arrays;

public class DisjointTest {
	static int n = 7;
	static int[] parents = new int[n];
	
	static void makeSet() {
		for (int i = 0; i < n; i++) {
			parents[i] = i;
		}
	}
	static int findSet(int v) {
		if(v == parents[v]) return v;
		return parents[v] = findSet(v);
	}
	static void unionSet(int v, int u) {
		parents[findSet(u)] = findSet(v);
		System.out.println(Arrays.toString(parents));
	}
	public static void main(String[] args) {
		makeSet();
		unionSet(3, 4);
		unionSet(3, 5);
		unionSet(3, 6);
	}

}
